from datetime import datetime
import random


# compute the percentage of a nutrient between current value and target and round it up
def compute_percentage(nutrient_stats):       
    if not nutrient_stats:                      # if there is no entry, it is empty
        return -100
    else:
        return round(((int(nutrient_stats[0])*100)/int(nutrient_stats[1])) - 100)


# check if it is almost end of day
def is_end_of_day():
    return True if datetime.now().time().hour >= 21 else False


# compute calorie percentage and return the text based on the NL_level
def get_calories(today, calories_dict, user_NL_level):
    percentage = compute_percentage(calories_dict)

    print("percentage: ", percentage)

    if is_end_of_day():                                                     # it is the end of the day and
        if percentage > 0:                                                  # the user is over his daily calorie intake
            if user_NL_level == 1:
                text = "higher than your target."
            elif user_NL_level == 2 or user_NL_level == 3:
                text = str(abs(percentage)) + "% higher than your target."
        elif -60 < percentage < 0:                                          # the user is between minus 0-60% of his daily calorie intake  
            if user_NL_level == 1:
                text = "lower than your target. " 
            elif user_NL_level == 2 or user_NL_level == 3:
                text = str(abs(percentage)) + "% lower than your target. " 

            if today:     #if the requested information was about today
                text += "Good job! 🔝\n\nHow about a small snack though to reach your goal?!"
            else:
                text += "Good job! 🔝\n\nAlthough, next time, you could try having a small snack to reach your goal."
        else:                                                              # the user is between minus 60-10% of his daily calorie intake
            if user_NL_level == 1:
                text = "lower than your target. " 
            elif user_NL_level == 2 or user_NL_level == 3:
                text = str(abs(percentage)) + "% lower than your target. " 

            if today:
                text += random.choice(["You have logged a very small amount of food. Did you forget to eat today?!",
                        "You have logged a very small amount of food. You must be starving by now 🤔"])
            else:
                text += "You logged a very small amount of food. Did you forget to eat back then?!"
    else:                                                                   # it is before 9pm and
        if percentage > 0:                                                  # the user is over his daily calorie intake
            if user_NL_level == 1:
                text = "higher than your target."
            elif user_NL_level == 2 or user_NL_level == 3:
                text = str(abs(percentage)) + "% higher than your target."
        else:                                                               # the user is minus 0-100% of his daily calorie intake
            if user_NL_level == 1:                                          # but here the percentage doesn't matter,
                text = "lower than your target. "                           
            elif user_NL_level == 2 or user_NL_level == 3:
                text = str(abs(percentage)) + "% lower than your target. " 

            if today:    # the user can still eat a lot during the day
                text += "Good job! 🔝\n\nTry getting the rest by the end of today though!"
            else:                                                             # the user didn't eat much
                text += "You logged a very small amount of food. Did you forget to eat back then?!"

    return text


# find and return the to 2 good nutrients
def get_good_nutr(user_date_stats):         
    if (user_date_stats["calories"][1] == user_date_stats["calories"][2]):  # if there were no entries for the date requested
        print("0 entries")
        return 0

    new_stats_dic = dict(user_date_stats)   # take the dict with the nutrient
    del new_stats_dic["calories"]           # remove the 'calories'
   
    for key in new_stats_dic.items():
        percentage = compute_percentage(new_stats_dic[key[0]])  # sort it by percentage               
        new_stats_dic[key[0]].append(percentage)

    good_nutr = dict(sorted(new_stats_dic.items(), key=lambda r: r[1][2], reverse=True)[:2])  # and return the top 2 good nutrients

    return good_nutr


# find and return the to 2 bad nutrients
def get_bad_nutr(user_date_stats):          
    if (user_date_stats["calories"][1] == user_date_stats["calories"][2]):  # if there were no entries for the date requested
        print("0 entries")
        return 0
 
    new_stats_dic = dict(user_date_stats)   # take the dict with the nutrients
    del new_stats_dic["calories"]           # remove the 'calories'

    for key in new_stats_dic.items():
        percentage = compute_percentage(new_stats_dic[key[0]])       # sort the dict by percentage
        new_stats_dic[key[0]].append(percentage)

    bad_nutr = dict(sorted(new_stats_dic.items(), key=lambda r: r[1][2]) [:2])  # and return the top 2 bad nutrients

    return bad_nutr


# return recommended food examples based on the nutrient
def get_food_examples(nutrient):
    if nutrient == 'carbohydrates':
        return random.choice(["bread", "rice", "pasta", "potatoes", "cereals"])
    elif nutrient == 'protein':
        return random.choice(["vegetables like tomatoes, broccoli, leafy greens", "fruits like apples, bananas, pears, peaches", "grains like rice, oats, rice, pasta"])
    elif nutrient == 'fat':
        return random.choice(["processed food", "oil", "margarine", "cheese", "sausage", "biscuits, cakes, and pastries"])
    elif nutrient == 'sodium':
        return random.choice(["ready-made food", "sausages", "salt", "potato chips", "frozen pizzas", "canned food", "fast food"])
    elif nutrient == 'sugar':
        return random.choice(["ready-made products", "salad dressings", "sweet drinks such as soft drinks", "sweets and pastries"])


# return recommended food groups to shift to based on nutrient
def get_food_group_examples_less(nutrient):
    if nutrient == 'carbohydrates':                                   # to avoid repetition, all nutrients offer the same recommendations
        return random.choice(["nuts and seeds", "fats and oils"])     # except carbs and fat
    elif nutrient == 'fat':
        return random.choice(["grains"])
    else:
        return random.choice(["fruits", "vegetables"])


# return recommended food groups to increase based on nutrient
def get_food_group_examples_more(nutrient):
    if nutrient == 'carbohydrates':
        return random.choice(["nuts and seeds", "fats and oils"])
    elif nutrient == 'sugar':
        return random.choice(["fruits and vegetables that are a natural source of sugar"])
    elif nutrient == 'fat':
        return random.choice(["fatty products and oils"])
    elif nutrient == 'sodium':
        return random.choice(["grains"])
    elif nutrient == 'protein':
        return random.choice(["dairy products"])


# return the proper volume adjective based on the user's input
def get_volume_adjective(volume_input):
    if volume_input == "TOP":
        return " highest "
    else:
        return " lowest "


# return the reverse volume adjective based on the user's input
def get_volume_adjective_reverse(volume_input):
    if volume_input == "TOP":
        return " less "
    else:
        return " more "


# return the correct measure based on the nutrient
def get_grams(nutrient):
    if nutrient == 'sodium':            # 'sodium' is measured in mgrams
        return " mgrams"
    elif nutrient == 'calories':
        return " kcal"
    else:
        return " grams"


# calculate the percentage between the current stat and the target
def get_percentage(current, target):
    return str(round(current*100/target - 100))


# replace nutrient names based on the user's NL level
def replace_nutrient(text, user_NL_level):
    if user_NL_level == 1:
        text = text.replace('sodium', 'salt')
        text = text.replace('Sodium', 'Salt')
    else:
        text = text.replace('salt', 'sodium')
        text = text.replace('Salt', 'Sodium')

    return text
