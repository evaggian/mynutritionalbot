import random

from sympy import re 

def compute_percentage(nutrient_stats):         # compute the percentage of a nutrient between current value and target and round it up
    print(nutrient_stats[0])
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

def get_good_nutr(user_date_stats):         # take the dic with the nutrients, remove the 'calories', sort it by percentage               
    new_stats_dic = dict(user_date_stats)   # and return the top 2 good nutrients
    del new_stats_dic["calories"]
    
    for key in new_stats_dic.items():
        percentage = compute_percentage(new_stats_dic[key[0]])
        new_stats_dic[key[0]].append(percentage)

    good_nutr = dict(sorted(new_stats_dic.items(), key=lambda r: r[1][2], reverse = True)[:2])

    return good_nutr

def get_bad_nutr(user_date_stats):          # take the dic with the nutrients, remove the 'calories', sort it by percentage
    new_stats_dic = dict(user_date_stats)   # and return the top 2 bad nutrients
    del new_stats_dic["calories"]
    
    for key in new_stats_dic.items():
        percentage = compute_percentage(new_stats_dic[key[0]])
        new_stats_dic[key[0]].append(percentage)

    bad_nutr = dict(sorted(new_stats_dic.items(), key=lambda r: r[1][2]) [:2])
    print(bad_nutr)

    return bad_nutr


def get_food_examples(nutrient):
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

def get_volume_adjective(volume_input):
    if volume_input == "TOP":
        return " highest "
    else:
        return " lowest "

def get_volume_adjective_reverse(volume_input):
    if volume_input == "TOP":
        return " less "
    else:
        return " more "

def get_grams(nutrient):
    if nutrient == 'sodium':
        return " mg"
    else:
        return " g"
