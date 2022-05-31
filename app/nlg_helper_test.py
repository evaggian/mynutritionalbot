from nlg_helper import get_bad_nutr, get_good_nutr, get_percentage, compute_percentage, is_end_of_day, get_calories


def test_get_percentage():
    assert get_percentage(20, 80) == "-75"


def test_get_percentage_no_entry():
    assert get_percentage(0, 80) == "-100"


def test_compute_percentage_lower():
    nutrient_stats = [234.0, 1720.0, 1486.0]
    assert compute_percentage(nutrient_stats) == -86


def test_compute_percentage_higher():
    nutrient_stats = [2000.0, 1720.0, -280.0]
    assert compute_percentage(nutrient_stats) == 16


def test_compute_percentage_empty():
    nutrient_stats = []
    assert compute_percentage(nutrient_stats) == -100


def test_is_end_of_day():
    assert is_end_of_day() == False


def test_get_calories_is_end_of_day(mocker):
    errors = []
    mocker.patch('nlg_helper.is_end_of_day', return_value=True)

    calories_dict_86 = [234.0, 1720.0, 1486.0]         # -86%
    calories_dict_28 = [1234.0, 1720.0, 486.0]         # -28%
    calories_dict_16 = [2000.0, 1720.0, -280.0]        #  17%

    lvl_1_86 = get_calories(calories_dict_86, 1)
    r1 = "lower than your target. You have logged a very small amount of food. Did you forget to eat today?!"
    r2 = "lower than your target. You have logged a very small amount of food. You must be starving by now 🤔"

    lvl_2_86 = get_calories(calories_dict_86, 2)
    r3 = "86% lower than your target. You have logged a very small amount of food. Did you forget to eat today?!"
    r4 = "86% lower than your target. You have logged a very small amount of food. You must be starving by now 🤔"

    lvl_1_28 = get_calories(calories_dict_28, 1)
    r5 = "lower than your target. Good job! 🔝\n\n How about a small snack though to reach your goal?!"

    lvl_2_28 = get_calories(calories_dict_28, 2)
    r6 = "28% lower than your target. Good job! 🔝\n\n How about a small snack though to reach your goal?!"

    lvl_1_16 = get_calories(calories_dict_16, 1)
    r7 = "higher than your target."

    lvl_2_16 = get_calories(calories_dict_16, 2)
    r8 = "16% higher than your target."

    # replace assertions by conditions
    if not lvl_1_86 in (r1, r2):
        errors.append("failed test - lvl_1_86")
    if not lvl_2_86 in (r3, r4):
        errors.append("failed test - lvl_2_86")
    if not lvl_1_28 == r5:
        errors.append("failed test - lvl_1_28")
    if not lvl_2_28 == r6:
        errors.append("failed test - lvl_2_28")
    if not lvl_1_16 == r7:
        errors.append("failed test - lvl_1_16")
    if not lvl_2_16 == r8:
        errors.append("failed test - lvl_2_16")

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_get_calories_is_not_end_of_day(mocker):
    errors = []
    mocker.patch('nlg_helper.is_end_of_day', return_value=False)

    calories_dict_86 = [234.0, 1720.0, 1486.0]         # -86%
    calories_dict_16 = [2000.0, 1720.0, -280.0]        #  17%

    lvl_1_86 = get_calories(calories_dict_86, 1)
    r1 = "lower than your target. Good job! 🔝\n\nTry getting the rest by the end of today though!"

    lvl_2_86 = get_calories(calories_dict_86, 2)
    r2 = "86% lower than your target. Good job! 🔝\n\nTry getting the rest by the end of today though!"

    lvl_1_16 = get_calories(calories_dict_16, 1)
    r3 = "higher than your target."

    lvl_2_16 = get_calories(calories_dict_16, 2)
    r4 = "16% higher than your target."

    # replace assertions by conditions
    if not lvl_1_86 == r1:
        errors.append("failed test - lvl_1_86")
    if not lvl_2_86 == r2:
        errors.append("failed test - lvl_2_86")
    if not lvl_1_16 == r3:
        errors.append("failed test - lvl_1_16")
    if not lvl_2_16 == r4:
        errors.append("failed test - lvl_2_16")

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_get_good_nutr():
    user_date_stats = {'calories': [234.0, 1720.0, 1486.0], 'carbohydrates': [12.0, 215.0, 203.0], 'fat': [21.0, 57.0, 36.0], 'protein': [3.0, 86.0, 83.0], 'sodium': [10.0, 2300.0, 2290.0], 'sugar': [1.0, 65.0, 64.0]}
    good_nutrient = get_good_nutr(user_date_stats)
    assert good_nutrient == {'sodium': [10.0, 2300.0, 2290.0, -100], 'carbohydrates': [12.0, 215.0, 203.0, -94]}


def test_get_good_nutr_no_entries():
    user_date_stats = {'calories': [0, 2340.0, 2340.0], 'carbohydrates': [0, 293.0, 293.0], 'fat': [0, 78.0, 78.0], 'protein': [0, 117.0, 117.0], 'sodium': [0, 2300.0, 2300.0], 'sugar': [0, 88.0, 88.0]}
    good_nutrient = get_good_nutr(user_date_stats)
    assert good_nutrient == 0


def test_get_bad_nutr():
    user_date_stats = {'calories': [234.0, 1720.0, 1486.0], 'carbohydrates': [12.0, 215.0, 203.0], 'fat': [21.0, 57.0, 36.0], 'protein': [3.0, 86.0, 83.0], 'sodium': [10.0, 2300.0, 2290.0], 'sugar': [1.0, 65.0, 64.0]}
    bad_nutrient = get_bad_nutr(user_date_stats)
    assert bad_nutrient == {'fat': [21.0, 57.0, 36.0, -63], 'sugar': [1.0, 65.0, 64.0, -98]}


def test_get_bad_nutr_no_entries():
    user_date_stats = {'calories': [0, 2340.0, 2340.0], 'carbohydrates': [0, 293.0, 293.0], 'fat': [0, 78.0, 78.0], 'protein': [0, 117.0, 117.0], 'sodium': [0, 2300.0, 2300.0], 'sugar': [0, 88.0, 88.0]}
    bad_nutrient = get_bad_nutr(user_date_stats)
    assert bad_nutrient == 0
