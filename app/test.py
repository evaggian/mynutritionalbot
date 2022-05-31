import datetime

date_list = [datetime.date(2022, 5, 31)]
print(date_list[0])
if len(date_list) == 1 and date_list[0] == datetime.date.today():
    print("today")
else: print('other day')
