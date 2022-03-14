from math import remainder
import myfitnesspal
import calendar
import datetime
from datetime import date, timedelta

client = myfitnesspal.Client('evaggiab', password="myChatbot2022")

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

# retrieve totals, goals and remainder stats (5 nutrients + calories)
def get_info(user_name, date_input, nutrient):

    #TODO: identiify 'date' parameter = convert it from text to 2 days or 1 date

    # if date is single date
    if date_input == 'today':
        friend_current_stats = client.get_date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, username=user_name)
        remainder_stats = calculate_remainder(friend_current_stats.totals, friend_current_stats.goals)
        #print(remainder_stats)
        return remainder_stats

    # if it is a comparison between dates
    else:
        start_date = date(2022, 2, 27)
        end_date = date(2022, 3, 5)

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
        avg_totals = {key: round(totals.get(key, 0) / no_entries, 1)      
            for key in set(totals)}

        # calculate average goals among the duration of days and round it to 1 digit 
        print(int((end_date - start_date).days +1))
        avg_goals = {key: round(goals.get(key, 0) / int((end_date - start_date).days + 1), 1)        
            for key in set(goals)}

        # calculate average remainder
        avg_remainder = calculate_remainder(avg_totals, avg_goals)     

        print(avg_totals)
        print(avg_goals)
        print(avg_remainder)

        return avg_remainder

#get_info('evaggiab', 'today','overview')   
