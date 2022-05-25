import random

from app.myfitnesspal_db import get_date_stats 
from app.nlg_helper import get_bad_nutr, get_good_nutr, get_calories, get_food_examples, replace_nutrient, get_food_group_examples_less, get_food_group_examples_more, get_grams, get_volume_adjective, get_volume_adjective_reverse, get_percentage


def inform_overview(nutrient_list, date_list, insight, user_NL_level, user_name, user_first_name):

    user_date_stats = get_date_stats(user_name, date_list, insight)     # retrieve all stats of the requuested date

    if user_date_stats == -1:       # if the profile is private, return error message
        return -1
    elif user_date_stats is None:   # there are no entries for the date specified
        return None

    if not nutrient_list:
        return get_overview_text(user_NL_level, user_first_name, user_date_stats)   # return nlg text - overview
    else:
        return get_specific_nutrient_stats(nutrient_list, user_NL_level, user_date_stats)  # return nlg text - specific nutrient


def get_overview_text(user_NL_level, user_first_name, user_date_stats):
    good_nutr = get_good_nutr(user_date_stats)      # retrieve top 2 nutrient data that have positive values
    bad_nutr = get_bad_nutr(user_date_stats)        # retrieve top 2 nutrient data that have negative values

    if good_nutr == 0 or bad_nutr == 0:          # there are 0 entries for the date specified
        return "There are no entries for the date specified. Please choose a different day."

    if (bad_nutr[list(bad_nutr.keys())[0]][0]  < bad_nutr[list(bad_nutr.keys())[0]][1] and      # if there are no negative values, set no_bad_nutr to True
    bad_nutr[list(bad_nutr.keys())[1]][0] < bad_nutr[list(bad_nutr.keys())[1]][1]):
        no_bad_nutr = True
    else: no_bad_nutr = False


    if user_NL_level == 1:

        if no_bad_nutr:
            scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 1) + "\n" \
            + list(good_nutr.keys())[0].capitalize()  + " and " \
            + list(good_nutr.keys())[1]  + " are kept on a good level.\nSame for your " \
            + list(bad_nutr.keys())[0]  + " and " \
            + list(bad_nutr.keys())[1] + " intake.\n\n" \
            +  "Is everything clear to you? Do you have any further questions you'd like to ask me?"

            scenario_2 = "So, the good news is that " \
            + list(good_nutr.keys())[0] + " and " \
            + list(good_nutr.keys())[1] + " are around the recommended intake. 🎉🎉\n\nSimilarly, your " \
            + list(bad_nutr.keys())[0] + " and " \
            + list(bad_nutr.keys())[1] + " are good and can help you achieve your goal.\n\n" \
            + "Would you like to ask something more?"

        else:
            scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 1) + "\n" \
            + list(good_nutr.keys())[0].capitalize()  + " and " \
            + list(good_nutr.keys())[1]  + " are kept on a good level.\n\nHowever, your " \
            + list(bad_nutr.keys())[0]  + " and " \
            + list(bad_nutr.keys())[1] + " intake needs a bit " \
            + random.choice(["of work", "of improvement"]) \
            + ".\nYou could consider eating" \
            + " less " + get_food_examples(list(bad_nutr.keys())[0]) + " and " \
            + "less " + get_food_examples(list(bad_nutr.keys())[1]) + ".\n\n" \
            +  "Is everything clear to you? Do you have any further questions you'd like to ask me?"

            scenario_2 = "So, the good news is that " \
            + list(good_nutr.keys())[0] + " and " \
            + list(good_nutr.keys())[1] + " are around the recommended intake. 🎉🎉\n\nHowever, you should consider cutting down on " \
            + list(bad_nutr.keys())[0] + " and " \
            + list(bad_nutr.keys())[1] + ", as it will not help you achieve your goal.\n\nHow about eating" \
            + " less " + get_food_examples(list(bad_nutr.keys())[0]) + " and" \
            + " less " + get_food_examples(list(bad_nutr.keys())[1]) + "?\n\nWould you like to ask something more?"

        return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])

    elif user_NL_level == 2:

        if no_bad_nutr:
            scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 2) + "\n\n" \
            + list(good_nutr.keys())[0].capitalize() + " and " \
            + list(good_nutr.keys())[1] + " are kept on a good level.\n\nSame for your " \
            + list(bad_nutr.keys())[0] + " and " \
            + list(bad_nutr.keys())[1] + " intake.\n\n" \
            +  "Is everything clear to you? Do you have any further questions you'd like to ask me?"

            scenario_2 = "So, the good news is that " \
            + list(good_nutr.keys())[0] + " (" \
            + str(good_nutr[list(good_nutr.keys())[0]][0]) + "/" \
            + str(good_nutr[list(good_nutr.keys())[0]][1]) \
            + get_grams(list(good_nutr.keys())[0]) + ") and " \
            + list(good_nutr.keys())[1] + " (" \
            + str(good_nutr[list(good_nutr.keys())[1]][0]) + "/" \
            + str(good_nutr[list(good_nutr.keys())[1]][1]) \
            + get_grams(list(good_nutr.keys())[1]) + ") are around the recommended intake. 🎉🎉\n\nSimilarly, your " \
            + list(bad_nutr.keys())[0] + " (" \
            + str(bad_nutr[list(bad_nutr.keys())[0]][0]) + "/" \
            + str(bad_nutr[list(bad_nutr.keys())[0]][1]) \
            + get_grams(list(bad_nutr.keys())[0]) + ") and " \
            + list(bad_nutr.keys())[1] + " (" \
            + str(bad_nutr[list(bad_nutr.keys())[1]][0]) + "/" \
            + str(bad_nutr[list(bad_nutr.keys())[1]][1])  \
            + get_grams(list(bad_nutr.keys())[1]) + ") are good and can help you achieve your goal.\n\n" \
            + "Would you like to ask something more?"

        else:
            scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 2) + "\n\n" \
            + list(good_nutr.keys())[0].capitalize() + " and " \
            + list(good_nutr.keys())[1] + " are kept on a good level.\n\nHowever, your " \
            + list(bad_nutr.keys())[0] + " and " \
            + list(bad_nutr.keys())[1] + " intake needs a bit " \
            + random.choice(["of work", "of improvement"]) \
            + ". You could consider eating" \
            + " more " + get_food_group_examples_less(list(bad_nutr.keys())[0]) + " and" \
            + " more " + get_food_group_examples_less(list(bad_nutr.keys())[1]) + ".\n\n" \
            +  "Is everything clear to you? Do you have any further questions you'd like to ask me?"""

            scenario_2 = "So, the good news is that " \
            + list(good_nutr.keys())[0] + " (" \
            + str(good_nutr[list(good_nutr.keys())[0]][0]) + "/" \
            + str(good_nutr[list(good_nutr.keys())[0]][1]) \
            + get_grams(list(good_nutr.keys())[0]) + ") and " \
            + list(good_nutr.keys())[1] + " (" \
            + str(good_nutr[list(good_nutr.keys())[1]][0]) + "/" \
            + str(good_nutr[list(good_nutr.keys())[1]][1]) \
            + get_grams(list(good_nutr.keys())[1]) + ") are around the recommended intake. 🎉🎉\n\nHowever, you should consider cutting down on " \
            + list(bad_nutr.keys())[0] + " and " \
            + list(bad_nutr.keys())[1] + " , as it will not help you achieve your goal. How about eating" \
            + " more " + get_food_group_examples_less(list(bad_nutr.keys())[0]) + " and" \
            + " more " + get_food_group_examples_less(list(bad_nutr.keys())[1]) + " for a healthy diet?\n\nWould you like to ask something more?"

        return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])


    elif user_NL_level == 3:
        if no_bad_nutr:
            scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 3) + "\n" \
            + "\nYou had " \
            + str(good_nutr[list(good_nutr.keys())[0]][0]) + " out of " \
            + str(good_nutr[list(good_nutr.keys())[0]][1]) \
            + get_grams(list(good_nutr.keys())[0]) + " of " \
            + list(good_nutr.keys())[0] + " and " \
            + str(good_nutr[list(good_nutr.keys())[1]][0]) + " out of " \
            + str(good_nutr[list(good_nutr.keys())[1]][1]) \
            + get_grams(list(good_nutr.keys())[1]) + " of " \
            + list(good_nutr.keys())[1] + " which is great!\n\nSame for your " \
            + list(bad_nutr.keys())[0] + " and " \
            + list(bad_nutr.keys())[1] + " intake (" \
            + str(bad_nutr[list(bad_nutr.keys())[0]][0])  + "/ " \
            + str(bad_nutr[list(bad_nutr.keys())[0]][1]) \
            + get_grams(list(bad_nutr.keys())[0]) + " and " \
            + str(bad_nutr[list(bad_nutr.keys())[1]][0])  + "/ " \
            + str(bad_nutr[list(bad_nutr.keys())[1]][1]) \
            + get_grams(list(bad_nutr.keys())[1]) \
            + " respectively).\n\n" \
            + "Is everything clear to you? Do you have any further questions you'd like to ask me?"


            scenario_2 = "So the good news is that " \
            + list(good_nutr.keys())[0] + " and " \
            + list(good_nutr.keys())[1] + " are on target.\n\nYou had " \
            + str(good_nutr[list(good_nutr.keys())[0]][0]) \
            + get_grams(list(good_nutr.keys())[0]) + " of " \
            + list(good_nutr.keys())[0] + " and " \
            + str(good_nutr[list(good_nutr.keys())[1]][0]) \
            + get_grams(list(good_nutr.keys())[1]) + " of " \
            + list(good_nutr.keys())[1] + " which are around the recommended intake (" \
            + str(good_nutr[list(good_nutr.keys())[0]][1]) \
            + get_grams(list(good_nutr.keys())[0]) + " and " \
            + str(good_nutr[list(good_nutr.keys())[1]][1]) \
            + get_grams(list(good_nutr.keys())[1]) + " for each) 🔝.\n\nSimilarly, your " \
            + list(bad_nutr.keys())[0] + " (" \
            + str(bad_nutr[list(bad_nutr.keys())[0]][0]) + "/" \
            + str(bad_nutr[list(bad_nutr.keys())[0]][1]) \
            + get_grams(list(bad_nutr.keys())[0]) + ") and " \
            + list(bad_nutr.keys())[1] + " (" \
            + str(bad_nutr[list(bad_nutr.keys())[1]][0]) + "/" \
            + str(bad_nutr[list(bad_nutr.keys())[1]][1]) \
            + get_grams(list(bad_nutr.keys())[1]) + ") " \
            + "are good and can help you achieve your goal.\n\nWould you like to ask something more?"

        else:
            scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 3) + "\n" \
            + "\nYou had " \
            + str(good_nutr[list(good_nutr.keys())[0]][0]) + " out of " \
            + str(good_nutr[list(good_nutr.keys())[0]][1]) \
            + get_grams(list(good_nutr.keys())[0]) + " of " \
            + list(good_nutr.keys())[0] + " and " \
            + str(good_nutr[list(good_nutr.keys())[1]][0]) + " out of " \
            + str(good_nutr[list(good_nutr.keys())[1]][1]) \
            + get_grams(list(good_nutr.keys())[1]) + " of " \
            + list(good_nutr.keys())[1] + " which is great!\n\nHowever, your " \
            + list(bad_nutr.keys())[0] + "(" \
            + str(bad_nutr[list(bad_nutr.keys())[0]][0]) \
            + get_grams(list(bad_nutr.keys())[0]) + ") and " \
            + list(bad_nutr.keys())[1] + "(" \
            + str(bad_nutr[list(bad_nutr.keys())[1]][0]) \
            + get_grams(list(bad_nutr.keys())[1]) + ") intake exceeded the recommended intake (" \
            + str(bad_nutr[list(bad_nutr.keys())[0]][0])  + "/ " \
            + str(bad_nutr[list(bad_nutr.keys())[0]][1]) \
            + get_grams(list(bad_nutr.keys())[0]) + " and " \
            + str(bad_nutr[list(bad_nutr.keys())[1]][0])  + "/ " \
            + str(bad_nutr[list(bad_nutr.keys())[1]][1]) \
            + get_grams(list(bad_nutr.keys())[1]) + " respectively). You could consider cutting down on these.\n\n" \
            + "Is everything clear to you? Do you have any further questions you'd like to ask me?"


            scenario_2 = "So the good news is that " \
            + list(good_nutr.keys())[0] + " and " \
            + list(good_nutr.keys())[1] + " are on target.\n\nYou had " \
            + str(good_nutr[list(good_nutr.keys())[0]][0]) \
            + get_grams(list(good_nutr.keys())[0]) + " of " \
            + list(good_nutr.keys())[0] + " and " \
            + str(good_nutr[list(good_nutr.keys())[1]][0]) \
            + get_grams(list(good_nutr.keys())[1]) + " of " \
            + list(good_nutr.keys())[1] \
            + " which are around the recommended intake (" \
            + str(good_nutr[list(good_nutr.keys())[0]][1]) \
            + get_grams(list(good_nutr.keys())[0]) + " and " \
            + str(good_nutr[list(good_nutr.keys())[1]][1]) \
            + get_grams(list(bad_nutr.keys())[1]) + " for each) 🔝.\n\nHowever, you should consider cutting down on " \
            + list(bad_nutr.keys())[0] + " and " \
            + list(bad_nutr.keys())[1] + ", as you had an additional " \
            + str(abs(bad_nutr[list(bad_nutr.keys())[0]][2])) \
            + get_grams(list(bad_nutr.keys())[0]) + " and " \
            + str(abs(bad_nutr[list(bad_nutr.keys())[1]][2])) \
            + get_grams(list(bad_nutr.keys())[1]) + " of them, and it will not help you achieve your goal.\n\nWould you like to ask something more?"


        return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])


def get_specific_nutrient_stats(nutrient_list , user_NL_level, user_date_stats):
    print("user_date_stats: ", user_date_stats)

    good_stats = True                   # if the value is positive give positive feadback
    for nutrient in nutrient_list:
        if user_date_stats[nutrient][2] <= 0: # if the value is positive give negative feadback
            good_stats = False

    if good_stats:
        if user_NL_level == 1:
            scenario_1 = "Your " \
            + nutrient_list[0] + " intake was kept on a good level. Keep up the good work 💪\n\n" \
            + "Want to know something else?"

            scenario_2 = "It looks good. Keep it up 😀\n\n" \
            + "Anything else I can help with?"

            return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])

        elif user_NL_level == 2:
            scenario_1 = "Your " + nutrient_list[0] + " intake was " \
            + str(user_date_stats[nutrient_list[0]][0]) \
            + " out of " + str(user_date_stats[nutrient_list[0]][1]) \
            + get_grams(nutrient_list[0]) \
            + " which is below your target. Perhaps you could consider eating more " \
            + get_food_group_examples_more(nutrient_list[0]) \
            + " for a healthy diet?\n\n" \
            + "Want to know something else?"

            scenario_2 = "It looks good. Keep it up 😀\n\n" \
            + "Anything else I can help with?"

            return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])

        elif user_NL_level == 3:
            scenario_1 = "Your " \
            + nutrient_list[0] \
            + " intake was " \
            + str(user_date_stats[nutrient_list[0]][0]) \
            + " out of " \
            + str(user_date_stats[nutrient_list[0]][1]) \
            + get_grams(nutrient_list[0]) \
            + ". That's good. Keep up the good work 💪" \
            + "Want to know something else?"

            scenario_2 = str(user_date_stats[nutrient_list[0]][0]) \
            + "/" \
            + str(user_date_stats[nutrient_list[0]][1]) \
            + get_grams(nutrient_list[0]) + "\n\n" \
            + "Looks good! Keep it up 😀\n\n" \
            + "Anything else I can help with?"

            return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])
        
    else:
        if user_NL_level == 1:
            scenario_1 = "Your " \
            + nutrient_list[0] \
            + " intake needs some improvement. Perhaps you could consider eating less " \
            + get_food_examples(nutrient_list[0]) + "?!\n\n" \
            + "Want to know something else?"

            scenario_2 = "Hmm, it seems that you have been eating a lot of " \
            + nutrient_list[0] \
            + " 😬. It would be better to reduce it.\n\n" \
            + "Anything else I can help with?"

            return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])

        elif user_NL_level == 2:
            scenario_1 = "Your " + nutrient_list[0] + " intake was " \
            + str(user_date_stats[nutrient_list[0]][0]) \
            + " out of " + str(user_date_stats[nutrient_list[0]][1]) \
            + get_grams(nutrient_list[0]) \
            + " which is above your target. Perhaps you could consider eating " \
            + get_food_group_examples_more(nutrient_list[0]) \
            + " for a healthy diet?\n\n" \
            + "Want to know something else?"

            scenario_2 = "Hmm, it seems that you have been eating a lot of " \
            + nutrient_list[0] \
            + "(" \
            + str(user_date_stats[nutrient_list[0]][0]) + "/" \
            + str(user_date_stats[nutrient_list[0]][1]) \
            + get_grams(nutrient_list[0]) + ")" \
            + " 😬. It would be better to reduce it.\n\n" \
            + "Anything else I can help with?"

            return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])

        elif user_NL_level == 3:
            scenario_1 = "Your " \
            + nutrient_list[0] \
            + " intake was " \
            + str(user_date_stats[nutrient_list[0]][0]) \
            + " out of " \
            + str(user_date_stats[nutrient_list[0]][1]) \
            + get_grams(nutrient_list[0]) \
            + ". It seems that this needs a bit of improvement to reach your goal." 

            scenario_2 = "Hmm, it seems that you have been eating " \
            + str(user_date_stats[nutrient_list[0]][0]) \
            + " of " + str(user_date_stats[nutrient_list[0]][1]) \
            + get_grams(nutrient_list[0]) \
            + "😬. It would be better to reduce it by " \
            + get_percentage(user_date_stats[nutrient_list[0]][0], user_date_stats[nutrient_list[0]][1]) + "%.\n\n""" \
            + "Anything else I can help with?"

            return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])


def get_food_info_nlg(food_info, user_NL_level, nutrient_list, volume_input):   # return nlg text about top/lowest food requested
    print(food_info)
    print(list( food_info.values())[0])
    if user_NL_level == 1:
        scenario_1 = "Of the foods you ate, " \
        + list(food_info.keys())[0] + " was the" \
        + get_volume_adjective(volume_input) \
        + "in " \
        + nutrient_list[0] \
        + ". Why don't you substitute it with" \
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

        return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])

    elif user_NL_level == 2:

        if volume_input == "TOP":                       # check if you should eat more or less from a food, and return the appropriate food group example
            food_group_example = get_food_group_examples_less(nutrient_list[0])
        else:
            food_group_example = get_food_group_examples_more(nutrient_list[0])

        scenario_1 = "Of the foods you ate, " \
        + list(food_info.keys())[0] \
        + " had the" \
        + get_volume_adjective(volume_input) \
        + nutrient_list[0] \
        + " (" \
        + str(list( food_info.values())[0]) + get_grams(nutrient_list[0]) \
        + "). Why don't you substitute it with" \
        + get_volume_adjective_reverse(volume_input) \
        + food_group_example + "?"

        scenario_2 = list(food_info.keys())[0] \
        + " with " \
        + str(list( food_info.values())[0]) + get_grams(nutrient_list[0]) \
        + " of " \
        + nutrient_list[0] \
        + ". I know that changing what you eat is hard but consider your goal. You could try shifting your balance to eating" \
        + get_volume_adjective_reverse(volume_input) \
        + food_group_example + "?"

        return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])

    elif user_NL_level == 3: 
        scenario_1 = "Of the foods you ate, " \
        + list(food_info.keys())[0] \
        + " was the" \
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

        return random.choice([replace_nutrient(scenario_1, user_NL_level), replace_nutrient(scenario_2, user_NL_level)])



def get_first_time_user_text(user_first_name):
    text = "Hello " + user_first_name + "!\n\n" \
    + "I am Avobot, I will be your personal nutritionist and can help you understand your nutrition stats from MyFitnessPal better.\n\n" \
    + "I can also provide you with additional information.\n\n" \
    + "For example, you can ask me, “How many calories did I eat last week?” or “Why do I need protein?”. Cool right?!\n\n" \
    + "So, how can I help you today?"

    return text