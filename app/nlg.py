import random

from matplotlib.transforms import Bbox
from app.myfitnesspal_db import *
from app.nlg_helper import *

def inform_overview( date_list ,insight, user_NL_level, user_name, user_first_name):

    user_date_stats = get_date_stats(user_name ,date_list ,insight)

    good_nutr = get_good_nutr(user_date_stats)
    bad_nutr = get_bad_nutr(user_date_stats)

    #print(good_nutr)
    #print("here: " , type(list(good_nutr.keys())[0]))
    #print(list(good_nutr.keys())[0])

    if user_NL_level == 1:
        scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 1) + "\n" \
        + list(good_nutr.keys())[0].capitalize()  + " and " \
        + list(good_nutr.keys())[1]  + " are kept on a good level.\n\nHowever, your " \
        + list(bad_nutr.keys())[0]  + " and " \
        + list(bad_nutr.keys())[1] + " intake needs a bit " \
        + random.choice(["of work", "of improvement"]) \
        + ".\nYou could consider eating" \
        + " less " + get_food_examples(list(bad_nutr.keys())[0]) + " and " \
        + " less " + get_food_examples(list(bad_nutr.keys())[1]) + ".\n\n" \
        +  "Is everything clear to you? Do you have any further questions you'd like to ask me?"""

        scenario_2 = "So, the good news is that " \
        + list(good_nutr.keys())[0] + " and " \
        + list(good_nutr.keys())[1] + " are around the recommended intake. 🎉🎉\n\nHowever, you should consider cutting down on " \
        + list(bad_nutr.keys())[0] + " and " \
        + list(bad_nutr.keys())[1] + ", as it will not help you achieve your goal.\n\nHow about eating" \
        + " less " + get_food_examples(list(bad_nutr.keys())[0]) + " and" \
        + " less " + get_food_examples(list(bad_nutr.keys())[1]) + "?\n\nWould you like to ask something more?"

        return random.choice([scenario_1, scenario_2])

    elif user_NL_level == 2:
        scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 2) + "\n\n" \
        + list(good_nutr.keys())[0].capitalize() + " and " \
        + list(good_nutr.keys())[1] + " are kept on a good level.\n\nHowever, your " \
        + list(bad_nutr.keys())[0] + " and " \
        + list(bad_nutr.keys())[1] + " intake needs a bit " \
        + random.choice(["of work", "of improvement"]) \
        + ". You could consider eating" \
        + " less " + get_food_examples(list(bad_nutr.keys())[0]) + " and" \
        + " less " + get_food_examples(list(bad_nutr.keys())[1]) + ".\n\n" \
        +  "Is everything clear to you? Do you have any further questions you'd like to ask me?"""

        scenario_2 = "So, the good news is that " \
        + list(good_nutr.keys())[0] + " (" \
        + str(good_nutr[list(good_nutr.keys())[0]][0]) + "/" \
        + str(good_nutr[list(good_nutr.keys())[0]][1]) + ") and " \
        + list(good_nutr.keys())[1] + " (" \
        + str(good_nutr[list(good_nutr.keys())[1]][0]) + "/" \
        + str(good_nutr[list(good_nutr.keys())[1]][1]) +")  are around the recommended intake. 🎉🎉\n\nHowever, you should consider cutting down on " \
        + list(bad_nutr.keys())[0] + " and " \
        + list(bad_nutr.keys())[1] + " , as it will not help you achieve your goal. How about eating " \
        + " less " + get_food_examples(list(bad_nutr.keys())[0]) + " and" \
        + " less " + get_food_examples(list(bad_nutr.keys())[1]) + " for a healthy diet?\n\nWould you like to ask something more?"""

        return random.choice([scenario_1, scenario_2])

    elif user_NL_level == 3:
        scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 3) + "\n" \
        + "\nYou had " \
        + str(good_nutr[list(good_nutr.keys())[0]][0]) + " out of " \
        + str(good_nutr[list(good_nutr.keys())[0]][1]) + " of " \
        + list(good_nutr.keys())[0] + " and " \
        + str(good_nutr[list(good_nutr.keys())[1]][0]) + " out of " \
        + str(good_nutr[list(good_nutr.keys())[1]][1]) + " of " \
        + list(good_nutr.keys())[1] + " which is great!\n\nHowever, your " \
        + list(bad_nutr.keys())[0] + "(" \
        + str(bad_nutr[list(bad_nutr.keys())[0]][0]) + ") and " \
        + list(bad_nutr.keys())[1] + "(" \
        + str(bad_nutr[list(bad_nutr.keys())[0]][1]) + ") intake exceeded the recommended intake (" \
        + str(bad_nutr[list(bad_nutr.keys())[0]][0])  + "/ " \
        + str(bad_nutr[list(bad_nutr.keys())[0]][1]) + " and " \
        + str(bad_nutr[list(bad_nutr.keys())[1]][0])  + "/ " \
        + str(bad_nutr[list(bad_nutr.keys())[1]][1]) + " respectively). You could consider cutting down on these.\n\n" \
        + "Is everything clear to you? Do you have any further questions you'd like to ask me?"


        scenario_2 = "So the good news is that " \
        + list(good_nutr.keys())[0] + " and " \
        + list(good_nutr.keys())[1] + " are on target.\n\nYou had " \
        + str(good_nutr[list(good_nutr.keys())[0]][0]) + " of " \
        + list(good_nutr.keys())[0] + " and " \
        + str(good_nutr[list(good_nutr.keys())[1]][0]) + " of " \
        + list(good_nutr.keys())[1] + " which are around the recommended intake (" \
        + str(good_nutr[list(good_nutr.keys())[1]][0]) + " and " \
        + str(good_nutr[list(good_nutr.keys())[1]][1]) + " for each) 🔝.\n\nHowever, you should consider cutting down on " \
        + list(bad_nutr.keys())[0] + " and " \
        + list(bad_nutr.keys())[1] + ", as you had an additional " \
        + str(bad_nutr[list(bad_nutr.keys())[0]][2]) + " and " \
        + str(bad_nutr[list(bad_nutr.keys())[1]][2]) + " of them, and it will not help you achieve your goal.\n\nWould you like to ask something more?"

        return random.choice([scenario_1, scenario_2])


def get_food_info_nlg(food_info, user_NL_level, nutrient_list, volume_input):
    print(food_info)
    print(list( food_info.values())[0])
    if user_NL_level == 1:
        scenario_1 = "Of the foods you ate, " \
        + list(food_info.keys())[0] + " was the " \
        + get_volume_adjective(volume_input) \
        + "in " \
        + nutrient_list[0] \
        + ". Why don't you substitute it with " \
        + get_volume_adjective_reverse(volume_input) \
        + get_food_examples(nutrient_list[0]) \
        + "?"

        scenario_2 = list(food_info.keys())[0] + "." \
        + " I know that changing what you eat is hard but consider your goal. You could try eating something with" \
        + get_volume_adjective_reverse(volume_input) \
        + nutrient_list[0] \
        + " next time, such as " \
        + get_food_examples(nutrient_list[0]) \
        + "."

        return random.choice([scenario_1, scenario_2])

    elif user_NL_level == 2:
        scenario_1 = "Of the foods you ate, " \
        + list(food_info.keys())[0] \
        + " had the " \
        + get_volume_adjective(volume_input) \
        + nutrient_list[0] \
        + " (" \
        + str(list( food_info.values())[0]) + get_grams(nutrient_list[0]) \
        + "). Why don't you substitute it with" \
        + get_volume_adjective_reverse(volume_input) \
        + "of " \
        + "$nutr_1_group."

        scenario_2 = list(food_info.keys())[0] \
        + " with " \
        + str(list( food_info.values())[0]) + get_grams(nutrient_list[0]) \
        + " of " \
        + nutrient_list[0] \
        + ". I know that changing what you eat is hard but consider your goal. You could try shifting your balance to eating " \
        + get_volume_adjective_reverse(volume_input) \
        + "$nutr_1_group."

        return random.choice([scenario_1, scenario_2])

    elif user_NL_level == 3: 
        scenario_1 = "Of the foods you ate, " \
        + list(food_info.keys())[0] \
        + " was the " \
        + get_volume_adjective(volume_input) \
        + "in " \
        + nutrient_list[0] \
        + " with " \
        + str(list( food_info.values())[0]) + get_grams(nutrient_list[0]) + "."

        scenario_2 = list(food_info.keys())[0] \
        + " with " \
        + str(list( food_info.values())[0]) + get_grams(nutrient_list[0]) \
        + " of " \
        + nutrient_list[0] \
        + ". I know that changing what you eat is hard but consider your goal."

        return scenario_2