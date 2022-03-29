import random

def get_fun_fact_protein():
    fun_facts_list = ["Protein is one of the basic components of food and makes all life possible." +
    "Amino acids are the building blocks of proteins. All of the antibodies and enzymes, " + 
    "and many of the hormones in the body, are proteins. They provide for the transport of nutrients, " + 
    "oxygen, and waste throughout the body. They provide the structure and contracting capability of muscles. " + 
    "They also provide collagen to connective tissues of the body and to the tissues of the skin, hair, and nails.",
    
    "About 30 to 35% of your diet should consist of protein. " + 
    "Since men tend to be muscular and usually weigh more than women, they require more protein."]

    return random.choice(fun_facts_list)

def get_more_info(nutrient_list):
    if (len(nutrient_list) > 0):
        for i in range(len(nutrient_list)):
            if (nutrient_list[i] == 'protein'):
                return get_fun_fact_protein()
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