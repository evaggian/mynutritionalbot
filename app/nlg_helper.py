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

def get_nutr_1(user_date_stats):
    return ""

def get_nutr_2(user_date_stats):
    return ""

def get_bad_nutr_1(user_date_stats):
    return ""

def get_bad_nutr_2(User_date_stats):
    return ""
