import datetime

list = [{'Avocado - Avocado, 1 medium': 3.0}, {'Coles lamp rump steaks - Lamp steak, 1 steak': 47.0}]

top = 0 
top_food = None
for index in range(len(list)):
    for key in list[index]:
        if list[index][key] > top:
            top = list[index][key]
            top_food = list[index]
        #print(list[index][key])

print(top_food)
