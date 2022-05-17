from nlg import *


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

    r1 = "Your protein intake was 70.0 out of 86.0 which is below your target. " \
        + "Perhaps you could consider eating more food_group_1 for a healthy diet?\n\n" \
        + "Want to know something else?"
    r2 = "It looks good. Keep it up 😀\n\n" \
        + "Anything else I can help with?"

    assert result in (r1,r2) 

def test_get_specific_stats_lvl_3_good():
    nutrient_list = ["protein"]
    user_NL_level = 3
    user_date_stats = {'calories': [657.0, 1720.0, 1063.0], 'carbohydrates': [32.0, 215.0, 183.0], 'fat': [26.0, 57.0, 31.0], 'protein': [70.0, 86.0, 16.0], 'sodium': [2.0, 2300.0, 2298.0], 'sugar': [22.0, 65.0, 43.0]}

    result = get_specific_nutrient_stats(nutrient_list, user_NL_level, user_date_stats)

    r1 = "Your protein intake was 70.0 out of 86.0 which is below your target. " \
        + "Perhaps you could consider eating more food_group_1 for a healthy diet?\n\n" \
        + "Want to know something else?"
    r2 = "70.0/86.0 grams\n\n" \
        + "Looks good! Keep it up 😀\n\n" \
        + "Anything else I can help with?"

    assert result in (r1,r2) 