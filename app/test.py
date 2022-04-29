good_nutr = {'carbohydrates': [213.0, 215.0, 2.0, -1], 
'fat': [112.0, 57.0, -55.0, 96], 
'protein': [72.0, 86.0, 14.0, -16], 
'sodium': [509.0, 2300.0, 1791.0, -78], 
'sugar': [127.0, 65.0, -62.0, 95]}


# 0 = current
# 1 = target
# 2 = remainder
# 3 = percentage

print(good_nutr['carbohydrates'][2])
print(list(good_nutr.keys())[0])       # get name of the nutrient
print(good_nutr[list(good_nutr.keys())[0]][2])    # get value (remainder) of the nuntrient

print(list(good_nutr.keys())[0]  + " and ")

print("Well, calorie-wise, you are " 

        + list(good_nutr.keys())[0]  + " and ")