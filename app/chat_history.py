from email import message
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC2b9035cb7313a35472b6b20cb24c7e46'
auth_token = '8b33af25d22bb329c85f46a27dc50fd1'
client = Client(account_sid, auth_token)

messages = client.messages.list(limit=200)

for record in messages:
    #print(record.sid)
    message = client.messages(record.sid).fetch()
    print(message.body)