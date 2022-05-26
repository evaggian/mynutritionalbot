import mysql.connector
import myfitnesspal
import csv
import schedule
import time
import config as cfg
from datetime import date, timedelta

db_name = cfg.mysql["db_name"]
yesterday = date.today() - timedelta(days=1)

client = myfitnesspal.Client(username=cfg.mfp["username"], password=cfg.mfp["password"])


# connect to the db
def connect_db():
    return mysql.connector.connect(
            host=cfg.mysql["host"],
            user=cfg.mysql["user"],
            password=cfg.mysql["password"]
        )


def retrieve_users():

    mychatbot_db = connect_db()
    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("SELECT username FROM " + db_name + ".`users`")
        records = mycursor.fetchall()

        return records

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed") 


def job():
    users = retrieve_users()

    with open('daily_nutrition_report.csv', 'w', encoding='UTF8') as f:

        for user in users:

            friend_today_stats = client.get_date(yesterday.year, yesterday.month, yesterday.day, username=user[0])

            for meal in friend_today_stats.meals:
                    for entry in meal:      

                        result = []
                        result.append(user[0])
                        result.append(yesterday.strftime("%d/%m/%Y"))
                        result.append(friend_today_stats.totals)
                        result.append(friend_today_stats.goals)
                        result.append(entry.name)
                        result.append(entry.totals)
                        print(result)

                        writer = csv.writer(f)

                    # write the header
                        writer.writerow(result)

    f.close()

schedule.every().minutes.do(job)
schedule.every(3).hours.do(job)
schedule.every().day.at("00:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)