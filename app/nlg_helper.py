import random

def compute_percentage(nutrient_stats):         # compute the percentage of a nutrient between current value and target and round it up
    if not nutrient_stats:                      # if there is no entry, it is empty
        return -100
    else:
        return round(((int(nutrient_stats[0])*100)/int(nutrient_stats[1])) - 100)

def get_calories(calories_dic, user_NL_level):  # compute calorie percentage and return the text based on the NL_level

    percentage = compute_percentage(calories_dic)
    print("Percentage: ", percentage)

    if percentage > 0:
        if user_NL_level == 1:
            text = "higher than your target."
        elif user_NL_level == 2 or user_NL_level == 3:
            text = str(percentage) + "% higher than your target."
    else:
        if user_NL_level == 1:
            text = "lower than your target. Good job! 🔝" 
        elif user_NL_level == 2 or user_NL_level == 3:
            text = str(percentage) + "% lower than your target. Good job! 🔝" 

    return text

def get_good_nutr(user_date_stats):         # find and return the to 2 good nutrients
    if (user_date_stats["calories"][1] == user_date_stats["calories"][2]):  # if there were no entries for the date requested
        print("0 entries")
        return 0

    new_stats_dic = dict(user_date_stats)   # take the dict with the nutrient
    del new_stats_dic["calories"]           # remove the 'calories'
    
    for key in new_stats_dic.items():
        percentage = compute_percentage(new_stats_dic[key[0]])  # sort it by percentage               
        new_stats_dic[key[0]].append(percentage)

    good_nutr = dict(sorted(new_stats_dic.items(), key=lambda r: r[1][2], reverse = True)[:2])  # and return the top 2 good nutrients

    return good_nutr

def get_bad_nutr(user_date_stats):          # find and return the to 2 bad nutrients
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


def get_food_examples(nutrient):        # return recommended food examples based on the nutrient
    if nutrient == 'carbohydrates':
        return random.choice([("bread" , "rice" , "pasta", "potatoes", "cereals")])
    elif nutrient == 'protein':
        return random.choice(["vegetables like tomatoes, broccoli, leafy greens", "fruits like apples, bananas, pears, peaches", "grains like rice, oats, rice, pasta"])
    elif nutrient == 'fat':
        return random.choice(["processed food", "oil", "margarine", "cheese", "sausage", "biscuits, cakes, and pastries"])
    elif nutrient == 'sodium':
        return random.choice(["ready-made food", "sausages", "salt", "potato chips", "frozen pizzas", "canned food", "fast food"])
    elif nutrient == 'sugar':
        return random.choice(["ready-made products", "salad dressings", "sweet drinks such as soft drinks", "sweets and pastries"])

def get_volume_adjective(volume_input):     # return the proper volume adjective based on the user's input
    if volume_input == "TOP":
        return " highest "
    else:
        return " lowest "

def get_volume_adjective_reverse(volume_input): # return the reverse volume adjective based on the user's input
    if volume_input == "TOP":
        return " less "
    else:
        return " more "

def get_grams(nutrient):                # return the correct measure based on the nutrient
    if nutrient == 'sodium':            # 'sodium' is measured in mgrams
        return " mgrams"
    else:
        return " grams"


def get_percentage(current, target):        # calculate the percentage between the current stat and the target
    return str(round(current*100/target - 100))
