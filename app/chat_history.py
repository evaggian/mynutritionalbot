from twilio.rest import Client
import twilio_config as cfg
from datetime import date

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# For more help check: https://www.twilio.com/docs/sms/tutorials/how-to-retrieve-and-modify-message-history-python

client = Client(cfg.twilio["account_sid"], cfg.twilio["auth_token"])

# retrieve the chat history of a user based on the user_name and phone_number provided
def retrieve_chat_history(user_name, phone_number):
    messages = client.messages.list(
                               date_sent=date.today(),
                               from_='whatsapp:' + phone_number,
                           )

    chat_list = []
    for record in messages:
        chat = {}
        message = client.messages(record.sid).fetch()

        chat["user_name"] = user_name
        chat["phone_number"] = phone_number
        chat["date_sent"] = message.date_sent.strftime("%m/%d/%Y, %H:%M:%S")
        chat["from"] = message.from_
        chat["to"] = message.to
        chat["body"] = message.body

        print(chat)
        chat_list.append(chat)
        print(chat_list)

    print("--------")
    print(chat_list)
    print("--------")
    return chat_list



