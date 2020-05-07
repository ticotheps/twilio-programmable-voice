from twilio.rest import Client
from decouple import config

TEST_ACCOUNT_SID = config("TEST_ACCOUNT_SID")
TEST_AUTH_TOKEN = config("TEST_AUTH_TOKEN")

ACCOUNT_SID = config("ACCOUNT_SID")
AUTH_TOKEN = config("AUTH_TOKEN")

MY_PHONE_NUMBER = config("MY_PHONE_NUMBER")
MY_TWILIO_NUMBER = config("MY_TWILIO_NUMBER")

client = Client(TEST_ACCOUNT_SID, TEST_AUTH_TOKEN)

message = client.messages.create(
    to=MY_PHONE_NUMBER, 
    from_=MY_TEST_NUMBER,
    body="Hello from Tico's MacBook Pro!")

print(message.sid)
