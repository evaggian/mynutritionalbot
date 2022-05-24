from nlg_helper import get_bad_nutr, get_good_nutr, get_percentage, compute_percentage


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
