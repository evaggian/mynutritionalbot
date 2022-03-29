import myfitnesspal
import mysql.connector
from datetime import timedelta
import database_config as cfg


client = myfitnesspal.Client('evaggiab', password="myChatbot2022")

def initialize_db():

    mychatbot_db = mysql.connector.connect(
        host=cfg.mysql["host"],
        user=cfg.mysql["user"],
        password=cfg.mysql["password"]
    )

    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS heroku_5f2973cbf7c2b89")
        mycursor.execute(""" CREATE TABLE IF NOT EXISTS `heroku_5f2973cbf7c2b89`.`users` (
            `id` INT NOT NULL,
            `username` VARCHAR(45) NOT NULL,
            `nl_level` INT NOT NULL,
            UNIQUE INDEX `id_UNIQUE` (`id` ASC),
            PRIMARY KEY (`id`),
            UNIQUE INDEX `username_UNIQUE` (`username` ASC))
            PACK_KEYS = Default; """)
        
        # add your dummy user
        #mycursor.execute("""INSERT INTO `heroku_5f2973cbf7c2b89`.`users` (`id`, `username`, `nl_level`) VALUES ('1', 'evabot22', '1');""")
        mychatbot_db.commit()

    except mysql.connector.Error as error:
        print("Failed to connect {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed")

#print(client._user_metadata["goal_displays"][0]["nutrients"])

# compare current and goal nutrient and return the remainder
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

# for the time range given, call get_top_food or get_low_food and return the information requested
def get_food_info(user_name, date_input, nutrient_list, volume):
    print("REQUESTS DATA FOR: " + user_name, date_input, nutrient_list,volume)

    if len(date_input) == 1:
        friend_current_stats = client.get_date(date_input[0].year, date_input[0].month, date_input[0].day, username=user_name)

        if volume == "TOP":
            for nutrient in nutrient_list:
                meals = friend_current_stats.meals
                top_food = get_top_food(meals, nutrient)
                print(top_food)
                return top_food
        elif volume == "LOW":
            for nutrient in nutrient_list:
                meals = friend_current_stats.meals
                low_food = get_low_food(meals, nutrient)
                print(low_food)
                return low_food

    else:
        start_date = date_input[0]
        end_date = date_input[1]

        print(start_date)
        print(end_date)

        # for every day between 2 dates, retrieve totals + goals and sum them up
        top_food_list = []
        low_food_list = []
        for single_date in daterange(start_date, end_date):
            friend_current_stats = client.get_date(single_date.strftime("%Y"), single_date.strftime("%m"), single_date.strftime("%d"), username=user_name)

            if volume == "TOP":
                for nutrient in nutrient_list:
                    meals = friend_current_stats.get_date(date_input[0].year, date_input[0].month, date_input[0].day).meals
                    top_food = get_top_food(meals, nutrient_list[nutrient])
                    top_food_list.append(top_food)
            elif volume == "LOW":
                for nutrient in nutrient_list:
                    meals = friend_current_stats.get_date(date_input[0].year, date_input[0].month, date_input[0].day).meals
                    low_food = get_low_food(meals, nutrient_list[nutrient])
                    low_food_list.append(low_food)
        
        print(top_food_list)
        print(low_food_list)
        return top_food_list

# retrieve totals, goals and remainder stats (5 nutrients + calories)
def get_date_stats(user_name, date_input, insight):

    print("REQUESTS DATA FOR: " + user_name, date_input, insight)

    if insight == "overview":
        # if date is single date
        if len(date_input) == 1:
            friend_current_stats = client.get_date(date_input[0].year, date_input[0].month, date_input[0].day, username=user_name)
            remainder_stats = calculate_remainder(friend_current_stats.totals, friend_current_stats.goals)
            return remainder_stats

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

            print(avg_totals)
            print(avg_goals)
            print(avg_remainder)

            return avg_remainder

    else:
        print("There is no 'insight' attribute specified")

#get_info('evaggiab', 'today','overview')  


def get_NL_level(user_name):
    
    mychatbot_db = mysql.connector.connect(
        host=cfg.mysql["host"],
        user=cfg.mysql["user"],
        password=cfg.mysql["password"]
    )
    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("SELECT nl_level from `heroku_5f2973cbf7c2b89`.`users` where username = %s", (user_name,))
        record = mycursor.fetchone()

        return record[0]

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed")