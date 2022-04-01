import mysql.connector
import database_config as cfg

# setup db and tables for the first time
def initialize_db():

    mychatbot_db = mysql.connector.connect(
        host=cfg.mysql["host"],
        user=cfg.mysql["user"],
        password=cfg.mysql["password"]
    )

    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS heroku_5f2973cbf7c2b89")
        mycursor.execute(""" CREATE TABLE IF NOT EXISTS `heroku_5f2973cbf7c2b89`.`users` (
            `id` INT NOT NULL,
            `username` VARCHAR(45) NOT NULL,
            `nl_level` INT NOT NULL,
            `phone_number` VARCHAR(13) NOT NULL,
            `first_name` VARCHAR(45) NOT NULL,
            UNIQUE INDEX `id_UNIQUE` (`id` ASC),
            PRIMARY KEY (`id`),
            UNIQUE INDEX `username_UNIQUE` (`username` ASC),
            UNIQUE INDEX `phone_number_UNIQUE` (`phone_number` ASC))
            PACK_KEYS = Default; """)

        mycursor.execute("""CREATE TABLE IF NOT EXISTS `heroku_5f2973cbf7c2b89`.`chats_history` (
            `id` INT NOT NULL,
            `user_id` INT NULL,
            `text` VARCHAR(1000) NULL,
            PRIMARY KEY (`id`),
            UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC));""")
        
        # add your dummy user
        #mycursor.execute("""INSERT INTO `heroku_5f2973cbf7c2b89`.`users` (`id`, `username`, `nl_level`) VALUES ('1', 'evabot22', '1');""")
        mychatbot_db.commit()

    except mysql.connector.Error as error:
        print("Failed to connect {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed")

#print(client._user_metadata["goal_displays"][0]["nutrients"])
def user_exists(phone_number):
    mychatbot_db = mysql.connector.connect(
        host=cfg.mysql["host"],
        user=cfg.mysql["user"],
        password=cfg.mysql["password"]
    )
    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("SELECT username from `heroku_5f2973cbf7c2b89`.`users` where phone_number = %s", (phone_number,))
        record = mycursor.fetchone()
        if (record == None):
            return False
        else:
            return record[0]

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed")

# check if the user starts chatting with the chatbot for the first time
def first_time(user_name):
    mychatbot_db = mysql.connector.connect(
        host=cfg.mysql["host"],
        user=cfg.mysql["user"],
        password=cfg.mysql["password"]
    )
    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("SELECT * from `heroku_5f2973cbf7c2b89`.`chats_history`, `heroku_5f2973cbf7c2b89`.`users`"
                        + "where chats_history.user_id = users.id and username = %s", (user_name,))
        records = mycursor.fetchall()
        print("First time: ", records)
        if not records:
            return True
        else:
            return False

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed")    


# get the first name of the user
def get_user_first_name(user_name):
    mychatbot_db = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"]
    )
    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("SELECT first_name from `heroku_5f2973cbf7c2b89`.`users` where username = %s", (user_name,))
        record = mycursor.fetchone()

        return record[0]

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed")

# retrieve the NL level of the user from the db
def get_NL_level(user_name):
    
    mychatbot_db = mysql.connector.connect(
        host=cfg.mysql["host"],
        user=cfg.mysql["user"],
        password=cfg.mysql["password"]
    )
    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("SELECT nl_level from `heroku_5f2973cbf7c2b89`.`users` where username = %s", (user_name,))
        record = mycursor.fetchone()

        return record[0]

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed")