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
            `first_time` VARCHAR(1) BINARY NOT NULL,         
            UNIQUE INDEX `id_UNIQUE` (`id` ASC),
            PRIMARY KEY (`id`),
            UNIQUE INDEX `username_UNIQUE` (`username` ASC),
            UNIQUE INDEX `phone_number_UNIQUE` (`phone_number` ASC))
            PACK_KEYS = Default; """)
        
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

# check if the user exists in the db, check by phone_number connected to it
def user_exists(phone_number):
    mychatbot_db = mysql.connector.connect(
        host=cfg.mysql["host"],
        user=cfg.mysql["user"],
        password=cfg.mysql["password"]
    )
    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("SELECT username FROM `heroku_5f2973cbf7c2b89`.`users` WHERE phone_number = %s", (phone_number,))
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
        mycursor.execute("SELECT first_time FROM `heroku_5f2973cbf7c2b89`.`users` WHERE username = %s", (user_name,))
        record = mycursor.fetchone()

        if int(record[0]) == 1:
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

# if the user start chatting for the first time, update the first_time column to 0
def update_first_time(user_name):
    mychatbot_db = mysql.connector.connect(
        host=cfg.mysql["host"],
        user=cfg.mysql["user"],
        password=cfg.mysql["password"]
    )
    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("UPDATE `heroku_5f2973cbf7c2b89`.`users` SET `first_time` = '0' WHERE username = %s", (user_name,))

        mychatbot_db.commit()

    except mysql.connector.Error as error:
        print("Failed to connect {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed")
 


"""# get the phone number of the user
def get_user_phone_number(user_name):

    mychatbot_db = mysql.connector.connect(
        host=cfg.mysql["host"],
        user=cfg.mysql["user"],
        password=cfg.mysql["password"]
    )

    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("SELECT phone_number FROM `heroku_5f2973cbf7c2b89`.`users` WHERE username = %s", (user_name,))
        record = mycursor.fetchone()
        print(record)

        return record[0]

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed")"""


# get the first name of the user
def get_user_first_name(user_name):
    mychatbot_db = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"]
    )
    try:
        mycursor = mychatbot_db.cursor()
        mycursor.execute("SELECT first_name FROM `heroku_5f2973cbf7c2b89`.`users` WHERE username = %s", (user_name,))
        record = mycursor.fetchone()
        print(record)

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
        mycursor.execute("SELECT nl_level FROM `heroku_5f2973cbf7c2b89`.`users` WHERE username = %s", (user_name,))
        record = mycursor.fetchone()

        return record[0]

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    
    finally:
        if mychatbot_db.is_connected():
            mycursor.close()
            mychatbot_db.close()
            print("MySQL connection is closed")