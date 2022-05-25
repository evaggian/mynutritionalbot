import random


# compute the percentage of a nutrient between current value and target and round it up
def compute_percentage(nutrient_stats):       
    if not nutrient_stats:                      # if there is no entry, it is empty
        return -100
    else:
        return round(((int(nutrient_stats[0])*100)/int(nutrient_stats[1])) - 100)


# compute calorie percentage and return the text based on the NL_level
def get_calories(calories_dic, user_NL_level):
    percentage = compute_percentage(calories_dic)

    if percentage > 0:
        if user_NL_level == 1:
            text = "higher than your target."
        elif user_NL_level == 2 or user_NL_level == 3:
            text = str(abs(percentage)) + "% higher than your target."
    else:
        if user_NL_level == 1:
            text = "lower than your target. Good job! 🔝" 
        elif user_NL_level == 2 or user_NL_level == 3:
            text = str(abs(percentage)) + "% lower than your target. Good job! 🔝" 

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
