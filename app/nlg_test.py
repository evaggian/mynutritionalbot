from nlg import *


#def test_gett_overview_text_no_entries()
# [TO-DO: write this test]

def test_get_overview_text_lvl_1_good():
    user_NL_level = 1
    user_first_name = "Test"
    user_date_stats = {'calories': [657.0, 1720.0, 1063.0], 'carbohydrates': [32.0, 215.0, 183.0], 'fat': [26.0, 57.0, 31.0], 'protein': [70.0, 86.0, 16.0], 'sodium': [2.0, 2300.0, 2298.0], 'sugar': [22.0, 65.0, 43.0]}

    result = get_overview_text(user_NL_level, user_first_name, user_date_stats)

    r1 = "Well, Test, calorie-wise, you are lower than your target. Good job! 🔝\n" \
        + "Salt and carbohydrates are kept on a good level.\n" \
        + "Same for your protein and fat intake.\n\n" \
        + "Is everything clear to you? Do you have any further questions you'd like to ask me?"

    r2 = "So, the good news is that salt and carbohydrates are around the recommended intake. 🎉🎉\n\n" \
        + "Similarly, your protein and fat are good and can help you achieve your goal.\n\n" \
        + "Would you like to ask something more?"

    assert result in (r1, r2)

"""def test_get_overview_text_lvl_1_bad():
    user_NL_level = 1
    user_first_name = "Test"
    user_date_stats = {'calories': [2078.0, 1720.0, -358.0], 'carbohydrates': [171.0, 215.0, 44.0], 'fat': [89.0, 57.0, -32.0], 'protein': [141.0, 86.0, -55.0], 'sodium': [98.0, 2300.0, 2202.0], 'sugar': [37.0, 65.0, 28.0]}

    result = get_overview_text(user_NL_level, user_first_name, user_date_stats)

    r1 = "So, the good news is that salt and carbohydrates are around the recommended intake. 🎉🎉\n\\n" \
        + "However, you should consider cutting down on protein and fat, as it will not help you achieve your goal.\n\n" \
        + "How about eating less fruits like apples, bananas, pears, peaches and less " \
        + "fruits like apples, bananas, pears, peaches?\n\n" \
        + "Would you like to ask something more?"

    r2 = "Well, Test, calorie-wise, you are higher than your target.\n" \
        + "Salt and carbohydrates are kept on a good level.\n\n" \
        + "However, your protein and fat intake needs a bit of work.\n" \
        + "You could consider eating less" \
        + "fruits like apples, bananas, pears, peaches and  less" \
        + "fruits like apples, bananas, pears, peaches.\n\n" \
        + "Is everything clear to you? Do you have any further questions you'd like to ask me?"

    assert result in (r1, r2)"""

def test_get_overview_text_lvl_2_good():
    user_NL_level = 2
    user_first_name = "Test"
    user_date_stats = {'calories': [170.0, 1720.0, 1550.0], 'carbohydrates': [14.0, 215.0, 201.0], 'fat': [0.0, 57.0, 57.0], 'protein': [2.0, 86.0, 84.0], 'sodium': [0.0, 2300.0, 2300.0], 'sugar': [0.0, 65.0, 65.0]}

    result = get_overview_text(user_NL_level, user_first_name, user_date_stats)

    r1 = "So, the good news is that sodium (0.0/2300.0 mgrams) and carbohydrates (14.0/215.0 grams) are around the recommended intake. 🎉🎉\n\n" \
        + "Similarly, your fat (0.0/57.0 grams) and sugar (0.0/65.0 grams) are good and can help you achieve your goal.\n\n" \
        + "Would you like to ask something more?"

    r2 = "Well, Test, calorie-wise, you are -90% lower than your target. Good job! 🔝\n\n" \
        + "Sodium and carbohydrates are kept on a good level.\n\n" \
        + "Same for your fat and sugar intake.\n\n" \
        + "Is everything clear to you? Do you have any further questions you'd like to ask me?"

    assert result in (r1, r2)


#def test_get_overview_text_lvl_2_bad():
# [TO-DO]: write this test

def test_get_overview_text_lvl_3_good():
    user_NL_level = 3
    user_first_name = "Test"
    user_date_stats = {'calories': [170.0, 1720.0, 1550.0], 'carbohydrates': [14.0, 215.0, 201.0], 'fat': [0.0, 57.0, 57.0], 'protein': [2.0, 86.0, 84.0], 'sodium': [0.0, 2300.0, 2300.0], 'sugar': [0.0, 65.0, 65.0]}

    result = get_overview_text(user_NL_level, user_first_name, user_date_stats)

    r1 = "So the good news is that sodium and carbohydrates are on target.\n\n" \
        + "You had 0.0 mgrams of sodium and 14.0 grams of carbohydrates which are around the recommended intake (2300.0 mgrams and 215.0 grams for each) 🔝.\n\n" \
        + "Similarly, your fat (0.0/57.0 grams) and sugar (0.0/65.0 grams) are good and can help you achieve your goal.\n\n" \
        + "Would you like to ask something more?"

    r2 = "Well, Test, calorie-wise, you are -90% lower than your target. Good job! 🔝\n\n" \
        + "You had 0.0 out of 2300.0 mgrams of sodium and 14.0 out of 215.0 grams of carbohydrates which is great!\n\n" \
        + "Same for your fat and sugar intake (0.0/ 57.0 grams and 0.0/ 65.0 grams respectively).\n\n" \
        + "Is everything clear to you? Do you have any further questions you'd like to ask me?"

    assert result in (r1, r2)

#def test_get_overview_text_lvl_3_bad():
# [TO-DO]: write this test

def test_get_specific_stats_lvl_1_good():
    nutrient_list = ["protein"]
    user_NL_level = 1
    user_date_stats = {'calories': [657.0, 1720.0, 1063.0], 'carbohydrates': [32.0, 215.0, 183.0], 'fat': [26.0, 57.0, 31.0], 'protein': [70.0, 86.0, 16.0], 'sodium': [2.0, 2300.0, 2298.0], 'sugar': [22.0, 65.0, 43.0]}

    result = get_specific_nutrient_stats(nutrient_list, user_NL_level, user_date_stats)

    r1 = "Your protein intake was kept on a good level. Keep up the good work 💪\n\n" \
        + "Want to know something else?"
    r2 = "It looks good. Keep it up 😀\n\n" \
        + "Anything else I can help with?"
        
    assert result in (r1,r2)

def test_get_specific_stats_lvl_2_good():
    nutrient_list = ["protein"]
    user_NL_level = 2
    user_date_stats = {'calories': [657.0, 1720.0, 1063.0], 'carbohydrates': [32.0, 215.0, 183.0], 'fat': [26.0, 57.0, 31.0], 'protein': [70.0, 86.0, 16.0], 'sodium': [2.0, 2300.0, 2298.0], 'sugar': [22.0, 65.0, 43.0]}

    result = get_specific_nutrient_stats(nutrient_list, user_NL_level, user_date_stats)

    r1 = "Your protein intake was 70.0 out of 86.0 grams which is below your target. " \
        + "Perhaps you could consider eating more dairy products for a healthy diet?\n\n" \
        + "Want to know something else?"
    r2 = "It looks good. Keep it up 😀\n\n" \
        + "Anything else I can help with?"

    assert result in (r1,r2) 

def test_get_specific_stats_lvl_3_good():
    nutrient_list = ["protein"]
    user_NL_level = 3
    user_date_stats = {'calories': [657.0, 1720.0, 1063.0], 'carbohydrates': [32.0, 215.0, 183.0], 'fat': [26.0, 57.0, 31.0], 'protein': [70.0, 86.0, 16.0], 'sodium': [2.0, 2300.0, 2298.0], 'sugar': [22.0, 65.0, 43.0]}

    result = get_specific_nutrient_stats(nutrient_list, user_NL_level, user_date_stats)

    r1 = "Your protein intake was 70.0 out of 86.0 grams. " \
        + "That's good. Keep up the good work 💪" \
        + "Want to know something else?"
    r2 = "70.0/86.0 grams\n\n" \
        + "Looks good! Keep it up 😀\n\n" \
        + "Anything else I can help with?"

    assert result in (r1,r2) 


def test_replace_nutrient():
    errors = []

    text_1 = replace_nutrient("sodium" , 1)
    text_2 = replace_nutrient("sodium", 2)
    text_3 = replace_nutrient("sodium", 3)
    text_4 = replace_nutrient("Sodium", 1)
    text_5 = replace_nutrient("Salt", 3)

    # replace assertions by conditions
    if not "salt" == text_1:
        errors.append("failed test - text_1")
    if not "sodium" == text_2:
        errors.append("failed test - text_2")
    if not "sodium" == text_3:
        errors.append("failed test - text_3")
    if not "Salt" == text_4:
        errors.append("failed test - text_4")
    if not "Sodium" == text_5:
        errors.append("failed test - text_5")
    

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))