from myfitnesspal_db import *
import datetime

def test_calculate_remainder():
    totals = {'calories': 657, 'carbohydrates': 32, 'fat': 26, 'protein': 70, 'sodium': 2, 'sugar': 22}
    goals = {'calories': 1720, 'carbohydrates': 215, 'fat': 57, 'protein': 86, 'sodium': 2300, 'sugar': 65}
    remainder = calculate_remainder(totals, goals)
    assert remainder == {'calories': 1063, 'carbohydrates': 183, 'fat': 31, 'protein': 16, 'sodium': 2298, 'sugar': 43}

def test_calculate_remainder_no_entries():
    totals = {'calories': 0, 'carbohydrates': 0, 'fat': 0, 'protein': 0, 'sodium': 0, 'sugar': 0}
    goals = {'calories': 1720, 'carbohydrates': 215, 'fat': 57, 'protein': 86, 'sodium': 2300, 'sugar': 65}
    remainder = calculate_remainder(totals, goals)
    assert remainder == {'calories': 1720, 'carbohydrates': 215, 'fat': 57, 'protein': 86, 'sodium': 2300, 'sugar': 65}

def test_get_top_food_no_entries():
    assert None == get_top_food(None, "protein")

def test_get_low_food_no_entries():
    assert None == get_low_food(None, "protein")

def test_get_top_food_list_empty():
    assert None == get_top_food_list(None)

def test_get_low_food_list_empty():
    assert None == get_low_food_list(None)

def test_get_top_food_list():
    top_food_list = [{'Coles lamp rump steaks - Lamp steak, 1 steak': 47.0}, {'Mora Kip Sate - Kip Sate, 180 gr': 23.0}]
    assert get_top_food_list(top_food_list) == {'Coles lamp rump steaks - Lamp steak, 1 steak': 47.0}

def test_get_low_food_list():
    top_food_list = [{'Coles lamp rump steaks - Lamp steak, 1 steak': 47.0}, {'Avocado': 4.0}, {'Mora Kip Sate - Kip Sate, 180 gr': 23.0}]
    assert get_low_food_list(top_food_list) == {'Avocado': 4.0}

def test_get_food_info_top():
    user_name = "evabot22"
    nutrient_list = 'protein'
    my_date = [datetime.date(2022, 5, 12)]
    volume = 'TOP'
    result = get_food_info(user_name, my_date, nutrient_list, volume)

    assert result == {'Coles lamp rump steaks - Lamp steak, 1 steak': 47.0}

def test_get_food_info_low():
    user_name = "evabot22"
    nutrient_list = 'protein'
    my_date = [datetime.date(2022, 5, 12)]
    volume = 'LOW'
    result = get_food_info(user_name, my_date, nutrient_list, volume)

    assert result == {'Mora Kip Sate - Kip Sate, 180 gr': 23.0}

def test_get_food_info_no_entries():
    user_name = "evabot22"
    nutrient_list = 'protein'
    my_date = [datetime.date(2022, 5, 3)]
    volume = 'TOP'
    result = get_food_info(user_name, my_date, nutrient_list, volume)

    assert result == None    

def test_get_food_info_top_two_dates():
    user_name = "evabot22"
    nutrient_list = 'protein'
    my_date = [datetime.date(2022, 5, 11), datetime.date(2022, 5, 12)]
    volume = 'TOP'
    result = get_food_info(user_name, my_date, nutrient_list, volume)

    assert result == {'Coles lamp rump steaks - Lamp steak, 1 steak': 47.0}

def test_get_food_info_low_two_dates():
    user_name = "evabot22"
    nutrient_list = 'sugar'
    my_date = [datetime.date(2022, 5, 11), datetime.date(2022, 5, 12)]
    volume = 'LOW'
    result = get_food_info(user_name, my_date, nutrient_list, volume)

    assert result == {'Avocado - Avocado, 1 medium': 1.0}

def test_get_food_info_no_entries_two_dates():
    user_name = "evabot22"
    nutrient_list = 'protein'
    my_date = [datetime.date(2022, 4, 1), datetime.date(2022, 4, 2)]
    volume = 'TOP'
    result = get_food_info(user_name, my_date, nutrient_list, volume)

    assert result == None   

def test_get_food_info_top():
    user_name = "evabot22"
    nutrient_list = 'protein'
    my_date = [datetime.date(2022, 5, 12)]
    volume = 'TOP'
    result = get_food_info(user_name, my_date, nutrient_list, volume)

    assert result == {'Coles lamp rump steaks - Lamp steak, 1 steak': 47.0}

def test_get_food_info_private_username():
    user_name = "biekvsbiypsnsliccm"
    nutrient_list = 'protein'
    my_date = [datetime.date(2022, 5, 12)]
    volume = 'TOP'
    result = get_food_info(user_name, my_date, nutrient_list, volume)

    assert result == -1

def test_get_food_info_private_username_two_dates():
    user_name = "biekvsbiypsnsliccm"
    nutrient_list = 'protein'
    my_date = [datetime.date(2022, 5, 11), datetime.date(2022, 5, 12)]
    volume = 'TOP'
    result = get_food_info(user_name, my_date, nutrient_list, volume)

    assert result == -1



