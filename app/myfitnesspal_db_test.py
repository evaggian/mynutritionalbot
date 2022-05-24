from myfitnesspal_db import calculate_remainder, get_top_food, get_low_food_list, get_date_stats, get_food_info, get_low_food, get_top_food_list
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
    assert None is get_top_food(None, "protein")


def test_get_low_food_no_entries():
    assert None is get_low_food(None, "protein")


def test_get_top_food_list_empty():
    assert None is get_top_food_list(None)


def test_get_low_food_list_empty():
    assert None is get_low_food_list(None)


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

    assert result is None    


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

    assert result is None


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


def test_get_date_stats():
    user_name = "evabot22"
    my_date = [datetime.date(2022, 5, 12)]
    insight = "overview"
    result = get_date_stats(user_name, my_date, insight)

    assert result == {'calories': [657.0, 1720.0, 1063.0], 'carbohydrates': [32.0, 215.0, 183.0], 'fat': [26.0, 57.0, 31.0], 'protein': [70.0, 86.0, 16.0], 'sodium': [2.0, 2300.0, 2298.0], 'sugar': [22.0, 65.0, 43.0]}


def test_get_date_stats_two_dates():
    user_name = "evabot22"
    my_date = [datetime.date(2022, 5, 11), datetime.date(2022, 5, 12)]
    insight = "overview"
    result = get_date_stats(user_name, my_date, insight)

    assert result == {'fat': [23.5, 57.0, 33.5], 'sodium': [6.0, 2300.0, 2294.0], 'carbohydrates': [22.0, 215.0, 193.0], 'sugar': [11.5, 65.0, 53.5], 'protein': [36.5, 86.0, 49.5], 'calories': [445.5, 1720.0, 1274.5]}


def test_get_date_stats_private_username():
    user_name = "biekvsbiypsnsliccm"
    my_date = [datetime.date(2022, 5, 12)]
    insight = "overview"
    result = get_date_stats(user_name, my_date, insight)

    assert result == -1


def test_get_date_stats_private_username_two_dates():
    user_name = "biekvsbiypsnsliccm"
    my_date = [datetime.date(2022, 5, 11), datetime.date(2022, 5, 12)]
    insight = "overview"
    result = get_date_stats(user_name, my_date, insight)

    assert result == -1


def test_get_date_stats_no_entries():
    user_name = "evabot22"
    my_date = [datetime.date(2022, 5, 1)]
    insight = "overview"
    result = get_date_stats(user_name, my_date, insight)

    assert result is None


def test_get_date_stats_no_entries_two_dates():
    user_name = "evabot22"
    my_date = [datetime.date(2022, 4, 1), datetime.date(2022, 4, 2)]
    insight = "overview"
    result = get_date_stats(user_name, my_date, insight)

    assert result is None
