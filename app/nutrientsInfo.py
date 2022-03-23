def get_more_info(nutrient_list):
    if (len(nutrient_list) > 0):
        for i in range(len(nutrient_list)):
            if (nutrient_list[i] == 'protein'):
                return "Protein is good for your body"
            elif (nutrient_list[i] == 'carbohydrates'):
                return "Carbs have to be kept very low"
            elif (nutrient_list[i] == 'fat'):
                return "Fat have to be kept very low"
            elif (nutrient_list[i] == 'sugar'):
                return "Carbs have to be kept very low"
            elif (nutrient_list[i] == 'sodium'):
                return "Sodium has to be below 2300mg per day"
            elif (nutrient_list[i] == 'calories'):
                return "Calories are important for you but try not to overdo it"