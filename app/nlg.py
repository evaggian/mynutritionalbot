import random
from app.myfitnesspal_db import *
from app.nlg_helper import *

def inform_overview(nutrient_list, date_list ,insight, user_NL_level, user_name, user_first_name):

    user_date_stats = get_date_stats(user_name ,date_list ,insight)

    if user_NL_level == 1:
        scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 1)

        """+ get_nutr_1(user_date_stats)  + "and "
        + get_nutr_2(user_date_stats)  + "are kept on a good level.\n However, your " 
        + get_bad_nutr_1(user_date_stats)  + "and " 
        + get_bad_nutr_2(user_date_stats) + "intake needs a bit " 
        + random.choice("of work", "of improvement") 
        + ". You could consider eating"
        + [more |less] $food_example_1 + "and "
        + [more |less] $food_example_2 + ".\n"
        +  "Is everything clear to you? Do you have any further questions you’d like to ask me?"

        scenario_2 = "So, the good news are that "
        + nutr_1 + "and"
        + nutr_2 + "are around the recommended intake. 🎉🎉\nAlthough, you should consider cutting down on" 
        + nutr_1 + "and "
        + nutr_2 + ", as it will not help you achieve your goal. How about eating" 
        + [more |less] food_example_1 + "and"
        + [more |less] food_example_2 + "?\"Would you like to ask something more?" """

    elif user_NL_level == 2:
        scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 2)
        """+ nutr_1 + "and" 
        + nutr_2 + "are kept on a good level.\n However, your"
        + nutr_1 + "and" 
        + nutr_2 + "intake needs a bit"
        + random.choice("of work", "of improvement") 
        + ". You could consider eating"
        + [more |less] $food_group_1 + "and 
        + [more |less] $food_group_2. + ".\n"
        +  "Is everything clear to you? Do you have any further questions you’d like to ask me?"

        scenario_2 = "So, the good news are that "
        + nutr_1 + "and "
        + nutr_2 + "are on target ("
        + nutr_1_value + "/" 
        + nutr_1_target + "and"
        + nutr_2_value + "/"
        + nutr_2_target +") are around the recommended intake. 🎉🎉\nAlthough, you should consider cutting down on "
        + nutr_1 + "and "
        + nutr_2 + ", as it will not help you achieve your goal. How about eating "
        + [more |less] food_group_1 + "and "
        + [more |less] food_group_2 + "for a healthy diet?\nWould you like to ask something more?"""

    elif user_NL_level == 3:
        scenario_1 = "Well, " + user_first_name + ", calorie-wise, you are " + get_calories(user_date_stats["calories"], 3)
    """     + "\n You had "
        + nutr_1_value + "out of "
        + nutr_1_value_target + "of " 
        + nutr_1 + "and "
        + nutr_2_value + "out of "
        + nutr_2_value_target + "of " 
        + nutr_2 + "which is great!\n However, your "
        + nutr_1 + "("
        + nutr_1_value + ") and "
        + nutr_2 + "("
        + nutr_2_value + ") intake exceeded the recommended intake ("
        + nutr_1_value  + "/ " 
        + nutr_1_target + "and ("
        + nutr_2_value  + "/ "
        + nutr_2_target + "respectively). You could consider cutting down on these.\n"
        + "Is everything clear to you? Do you have any further questions you’d like to ask me?"


        scenario_2 = "So the good news are that "
        + nutr_1 + "and "
        + nutr_2 + "are on target. You had "
        + nutr_1_value + "of "
        + nutr_1 + "and "
        + nutr_2_value + "of "
        + nutr_2 + "which are around the recommended intake ("
        + nutr_1_value_target + "and "
        + nut2_target + "for each) 🔝.\nAlthough, you should consider cutting down on "
        + nutr_1 + "and "
        + nutr_2 + ", as you had an additional " 
        + nutr_1_value_sup + "and "
        + nutrt2_value_sup + "of them, and it will not help you achieve your goal.\nWould you like to ask something more?" """

    return scenario_1