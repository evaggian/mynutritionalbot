from multiprocessing.connection import Client
import myfitnesspal
from datetime import timedelta
from collections import defaultdict
import database_config as cfg

client = myfitnesspal.Client(username=cfg.mfp["username"], password=cfg.mfp["password"])

# compare current and goal nutrient and return the remainder in a dict
def calculate_remainder(totals, goals):
    remainder = {key: round(goals[key] - totals.get(key, 0), 1) 
            for key in goals}
    return remainder

# calculate the daterange between 2 dates given
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

# calculate the food with the top nutrient among the entries in MFP
def get_top_food(meals, nutrient):
    top = 0
    top_food = None
    for meal in meals:          # meal={breakfast, lunch, dinner, snacks}
        for entry in meal:      # for every entry of this meal
                if (entry.totals[nutrient]) > top:
                    top = entry.totals[nutrient]
                    top_food = entry.name

    if (top_food == None): 
        return None
    else:
        return({top_food:top})  # return a dictionary with key the name of the food,
                                # and value the top value of the nutrient requested

# calculate the food with the lowest nutrient among the entries in MFP
def get_low_food(meals, nutrient):
    low = 100000
    low_food = None
    for meal in meals:          # meal={breakfast, lunch, dinner, snacks}
        for entry in meal:      # for every entry of this meal
                if (entry.totals[nutrient]) < low:
                    low = entry.totals[nutrient]
                    low_food = entry.name

    if (low_food == None): 
        return None
    else:
        return({low_food:low})  # return a dictionary with key the name of the food,
                                # and value the lowest value of the nutrient requested

# from a list of top food, find and return the toppest food by value
def get_top_food_list(top_food_list):          
    top = 0 
    top_food = None
    for index in range(len(top_food_list)):
        for key in top_food_list[index]:
            if top_food_list[index][key] > top:
                top = top_food_list[index][key]
                top_food = top_food_list[index]
    return(top_food)   

# from a list of low food, find and return the lowest food by value
def get_low_food_list(low_food_list):       
    low = 100000 
    low_food = None
    for index in range(len(low_food_list)):
        for key in low_food_list[index]:
            if low_food_list[index][key] < low:
                low = low_food_list[index][key]
                low_food = low_food_list[index]
    return(low_food)    

# for the time range given, call get_top_food or get_low_food and return the information requested
def get_food_info(user_name, date_input, nutrient, volume):
    print("REQUESTS DATA FOR: " + user_name, date_input, nutrient, volume)
    
    if len(date_input) == 1:        # if there is only one date specificed
        friend_current_stats = client.get_date(date_input[0].year, date_input[0].month, date_input[0].day, username=user_name)  #retrieve the information from MFP
         
        if not friend_current_stats.meals:      # if the profile is private, return error message
            return -1    

        if volume == "TOP":
            meals = friend_current_stats.meals
            top_food = get_top_food(meals, nutrient)
            print("top food: ", top_food)
            return top_food
        elif volume == "LOW":
            meals = friend_current_stats.meals
            low_food = get_low_food(meals, nutrient)
            print("low food: ", low_food)
            return low_food

    else:
        print(date_input[0])
        print(date_input[1])

        top_food_list = []
        low_food_list = []

        # for every day between 2 dates, retrieve totals + goals and sum them up
        for single_date in daterange(date_input[0], date_input[1]):
            friend_current_stats = client.get_date(single_date.strftime("%Y"), single_date.strftime("%m"), single_date.strftime("%d"), username=user_name)
            
            if not friend_current_stats.meals:      # if the profile is private, return error message
                return -1

            if volume == "TOP":
                meals = friend_current_stats.meals
                top_food = get_top_food(meals, nutrient)
                top_food_list.append(top_food)

            elif volume == "LOW":
                meals = friend_current_stats.meals
                low_food = get_low_food(meals, nutrient)
                low_food_list.append(low_food)

        if volume == "TOP":
            return get_top_food_list(top_food_list)
        elif volume == "LOW":
            return get_low_food_list(low_food_list)

# retrieve totals, goals and remainder stats (5 nutrients + calories)
def get_date_stats(user_name, date_input, insight):

    print("REQUESTS DATA FOR: " + user_name, date_input, insight)

    if insight == "overview":
        # if date is single date
        if len(date_input) == 1:
            friend_current_stats = client.get_date(date_input[0].year, date_input[0].month, date_input[0].day, username=user_name)

            if not friend_current_stats:      # if the profile is private, return error message
                return -1

            remainder_stats = calculate_remainder(friend_current_stats.totals, friend_current_stats.goals)

            if not friend_current_stats.totals:     # if this date's entry is empty, create a dict with 0 values
                totals = {'calories': 0, 'carbohydrates': 0, 'fat': 0, 'protein': 0, 'sodium': 0, 'sugar': 0}

                stats = defaultdict(list)       # create a dict combining dics from totals, goals and remainder

                for stat in (totals, friend_current_stats.goals, remainder_stats):
                    for key, value in stat.items():
                        stats[key].append(value)

            else:                           # if this date's entry has values
                stats = defaultdict(list)   # create a dict combining dics from totals, goals and remainder

                for stat in (friend_current_stats.totals, friend_current_stats.goals, remainder_stats):
                    for key, value in stat.items():
                        stats[key].append(value) 
    
            print("Stats:", stats)
            return stats

        # if it is a comparison between dates
        else:
            start_date = date_input[0]
            end_date = date_input[1]

            print(start_date)
            print(end_date)

            # initialize dictionaries with 0
            totals = dict.fromkeys(['calories','carbohydrates','fat','protein','sodium','sugar'], 0)
            goals = dict.fromkeys(['calories','carbohydrates','fat','protein','sodium','sugar'], 0)
            no_entries = 0

            # for every day between 2 dates, retrieve totals + goals and sum them up
            for single_date in daterange(start_date, end_date):
                friend_current_stats = client.get_date(single_date.strftime("%Y"), single_date.strftime("%m"), single_date.strftime("%d"), username=user_name)

                totals = {key: friend_current_stats.totals.get(key, 0) + totals.get(key, 0) 
                for key in set(friend_current_stats.totals) | set(totals)}

                # calculate how many days we have entries for
                if( friend_current_stats.totals.get("calories") != None):
                    no_entries += 1

                goals = {key: friend_current_stats.goals.get(key, 0) + goals.get(key, 0)
                for key in set(friend_current_stats.goals) | set(goals)}

            # calculate average totals among the number of days entried and round it to 1 digit
            # if there are no entries, create a dict with 0
            print(no_entries)
            if (no_entries == 0):
                avg_totals = {k: 0 for k in set(totals)}
            else:
                avg_totals = {key: round(totals.get(key, 0) / no_entries, 1)      
                for key in set(totals)}

            # calculate average goals among the duration of days and round it to 1 digit 
            avg_goals = {key: round(goals.get(key, 0) / int((end_date - start_date).days + 1), 1)        
                for key in set(goals)}

            # calculate average remainder
            avg_remainder = calculate_remainder(avg_totals, avg_goals)     

            stats = defaultdict(list)   # create a dict combining dics from totals, goals and remainder

            for stat in (avg_totals, avg_goals, avg_remainder):
                for key, value in stat.items():
                    stats[key].append(value) 

            print(stats)
            return stats

    else:
        print("There is no 'insight' attribute specified")

#get_info('evaggiab', 'today','overview')  