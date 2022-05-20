import random

def get_protein_scenario(user_NL_level):
    if user_NL_level == 1:
        scenarios = ["Protein is a crucial part of every cell in our bodies.\n\n" + 
        "It is particularly high in meat, fish, eggs, and dairy products (e.g., curd).\n\n" +
        "It is recommended to consume protein daily and in big quantities.",
        "Protein is necessary for many things. Whether you want to lose weight, gain muscle, " + 
        "recover from a challenging workout, feel more full at mealtime or simply keep healthy, " + 
        "it's important to get enough healthy protein.\n\n" + 
        "Protein is particularly high in meat, fish, eggs, and dairy products (e.g., curd).\n\n" + 
        "It is recommended to consume protein daily and in large quantities."]

        return random.choice(scenarios)

    elif user_NL_level == 2:
        scenarios = ["Protein is a crucial component of every cell in our bodies.\n\n" + 
        "It is particularly high in meat, fish, eggs, and dairy products (e.g., curd).\n\n" + 
        "Recommended intake: 10-35% of total daily energy.",
        "Protein is necessary for many things. It's essential to get adequate amounts of healthy protein, " + 
        "whether you want to lose weight, gain muscle, recover from a tough workout, feel more satiated at mealtime, " + 
        "or simply maintain good health.\n\n" + 
        "Recommended intake: 10-35% of total daily energy."]

        return random.choice(scenarios)

    elif user_NL_level == 3:
        scenarios = ["Protein is essential to maintaining a healthy and well-functioning body. " + 
        "The main role of protein in our body is to serve as 'building material' " + 
        "as it helps form and repair certain important substances and processes.\n\n" + 
        "Recommended intake: 10-35% of total daily energy.",
        "Protein is essential for many metabolic processes in the form of enzymes. \n\n" + 
        "Recommended intake: 10-35% of total daily energy."]

        return random.choice(scenarios)
    
def get_carb_scenario(user_NL_level):
    if user_NL_level == 1:
        scenarios = ["Our bodies need carbs, particularly glucose, since it's the preferred fuel for tissues and organs to perform essential functions.\n\n" + 
        "Bread, rice, pasta, potatoes, and cereals contain a lot of carbohydrates.\n\n" + 
        "You should consume carbohydrates daily but not in big portions.",
        "Carbohydrates (or “carbs”) are the primary energy source for our daily activities.\n\n" + 
        "Bread, rice, pasta, potatoes, and cereals contain a lot of carbohydrates.\n\n" +
        "You should consume carbohydrates daily but not in big portions."]

        return random.choice(scenarios)

    elif user_NL_level == 2:
        scenarios = ["Our bodies need carbs, particularly glucose, since it's the preferred fuel for tissues and organs to perform essential functions.\n\n" + 
        "Bread, rice, pasta, potatoes, and cereals contain a lot of carbohydrates.\n\n" +
        "The recommended daily intake is 45-65% of total energy.",
        "Carbohydrates (or “carbs”) are the primary energy source for our daily activities.\n\n" + 
        "Bread, rice, pasta, potatoes, and cereals contain a lot of carbohydrates.\n\n" + 
        "The recommended daily intake is 45-65% of total energy."]

        return random.choice(scenarios)

    elif user_NL_level == 3:
        scenarios = ["Carbohydrates are macronutrients that are most abundant in our diet. They are the main source of energy for our daily activities. \n\n" + 
        "The recommended daily intake is 45-65% of total energy.",
        "Carbohydrates or carbs divide into simple and complex. Simple carbohydrates ('sugars') " + 
        "are digested and absorbed into the bloodstream quickly, while complex carbohydrates (starch and fiber) are digested and absorbed slowly.\n\n" + 
        "The recommended daily intake is 45-65% of total energy."]

        return random.choice(scenarios)

def get_fat_scenario(user_NL_level):
    if user_NL_level == 1: 
        scenarios = ["A healthy amount of fat protects our cells, blood, and brain.\n\n" + 
        "It is found mainly in oil, butter, margarine, sweets, pastries, sausage, and cheese.\n\n" +
        "You should consume fat occasionally.",
        "Fat provides energy for our daily activities.\n\n" + 
        "It is found mainly in oil, butter, margarine, sweets, pastries, sausage, and cheese.\n\n" + 
        "You should consume fat occasionally."]

        return random.choice(scenarios)

    elif user_NL_level == 2:
        scenarios = ["Fats are macronutrients that, like carbohydrates, provide energy. A healthy amount of fat protects our cells, blood, and brain.\n\n" + 
        "It is found mainly in fat and oil products. The recommended daily intake is 20-35% of total energy.",
        "Fats are macros that provide energy for our daily activities.\n\n" + 
        "It is found mainly in oil, butter, margarine, sweets, pastries, sausage, and cheese.\n\n" +  
        "The recommended daily intake is 20-35% of total energy."]

        return random.choice(scenarios)

    elif user_NL_level == 3: 
        scenarios = ["Fats are macronutrients that, like carbohydrates, provide energy. " + 
        "Per gram, they provide more energy than carbohydrates and thus serve as energy stores in the body.\n\n" + 
        "Recommended intake: 20-35% of total energy.",
        "Fats are macros that provide energy. When energy intake is higher than consumption, " + 
        "fat accumulates and promotes the development of obesity.\n\n"
        "The recommended intake is 20-35% of total energy."]

        return random.choice(scenarios)    

def get_sugar_scenario(user_NL_level):
    if user_NL_level == 1: 
        scenarios = ["Eating too much sugar is related to a poor diet and excess calorie " + 
        "consumption contributing to weight gain.\n\n" + 
        "Sugar is very much in sweets, pastries, ready-made products, and sweet drinks such as soft drinks.\n\n" + 
        "You should consume sugar in small amounts or monthly.",
        "Sugar is a carbohydrate and is very much in sweets, pastries, ready-made products, " + 
        "and sweet drinks such as soft drinks.\n\n"
        "You should consume sugar in small amounts or monthly."]

        return random.choice(scenarios)

    elif user_NL_level == 2: 
        scenarios = ["Eating too much added sugar is related to poor dietary quality and possibly excess calorie consumption, " + 
        "contributing to weight gain.\n\n" + 
        "Sugar is very much in sweets, pastries, ready-made products, and sweet drinks such as soft drinks.\n\n" +
        "Recommended consumption: <5% of total energy",
        "Foods with added sugars are sometimes called foods with empty calories.\n\n" + 
        "Sugar is a carbohydrate and is very much in sweets, pastries, ready-made products, " + 
        "and sweet drinks such as soft drinks.\n\n" + 
        "The recommended consumption: <5% of total energy."]

        return random.choice(scenarios)
    
    elif user_NL_level == 3: 
        scenarios = ["Sugars are simple carbohydrates quickly digested and rapidly absorbed into the bloodstream. " + 
        "High sugar intake is associated with obesity and tooth decay.\n\n" + 
        "Recommended consumption: <5% of total energy.",
        "'Free sugars' such as monosaccharides (glucose and fructose) and disaccharides" + 
        "(sucrose and table sugar) are often added to food. They should be consumed in small amounts, " + 
        "as they have adverse health effects.\n\n" + 
        "The recommended consumption: <5% of total energy."]

        return random.choice(scenarios)


def get_sodium_scenario(user_NL_level):
    if user_NL_level == 1: 
        scenarios =  ["Sodium affects blood pressure, leading to heart problems in the long term. \n\n" + 
        "Sausages, snacks, fast food (e.g., French fries), and ready-made products (e.g., frozen pizza) have a lot of salt added.\n\n" +
        "It is recommended to consume it in small quantities daily.",
        "Sodium is found almost everywhere in the diet, so if you’re keeping an eye on your sodium counter, you probably know you don't need to eat salt to go extreme on your sodium levels.\n\n" + 
        "Sausages, snacks, fast food (e.g., French fries), and ready-made products (e.g., frozen pizza) have a lot of salt added.\n\n" + 
        "It is recommended to consume it in small quantities daily.",]

        return random.choice(scenarios)

    elif user_NL_level == 2: 
        scenarios =  ["The sodium content of salt is needed to regulate the amount of water in our bodies. \n\n" + 
        "However, sodium affects blood pressure, leading to cardiovascular problems in the long term. " + 
        "Recommended daily intake: < 3750 grams",
        "Sodium is found almost everywhere in the diet, so if you’re keeping an eye on your sodium counter, " + 
        "you probably know you don’t need to eat salt to go overboard on your sodium levels.\n\n" +
        "Sausages, snacks, fast food (e.g., French fries), and ready-made products (e.g., frozen pizza) have a lot of salt added.\n\n" + 
        "Recommended intake: < 3750 grams"]

        return random.choice(scenarios)

    elif user_NL_level == 3: 
        scenarios =  ["The sodium content of salt is needed to regulate the amount of water in our body, " + 
        "transmit signals from the nerves, and move the muscles. However, sodium intake is usually higher than recommended.\n\n" +
        "Recommended daily intake: < 3750 grams",
        "A large amount of sodium in the diet can cause high blood pressure, leading to an increased risk of cardiovascular" + 
        "disease and stroke. The high sodium content in food is 1.5g per 100g, and the low salt content is 0.3g per 100g. " + 
        "Always try to choose the lower salt product.\n\n" +
        "Recommended intake: < 3750 grams"]

        return random.choice(scenarios)



def get_more_info(nutrient_list, user_NL_level):
    if len(nutrient_list) > 0:
        for i in range(len(nutrient_list)):
            if (nutrient_list[i] == 'protein'):
                return get_protein_scenario(user_NL_level)
            elif (nutrient_list[i] == 'carbohydrates'):
                return get_carb_scenario(user_NL_level)
            elif (nutrient_list[i] == 'fat'):
                return get_fat_scenario(user_NL_level)
            elif (nutrient_list[i] == 'sugar'):
                return get_sugar_scenario(user_NL_level)
            elif (nutrient_list[i] == 'sodium'):
                return get_sodium_scenario(user_NL_level)
             