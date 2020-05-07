from twilio.rest import Client
from decouple import config

ACCOUNT_SID = config("ACCOUNT_SID")
AUTH_TOKEN = config("AUTH_TOKEN")

MY_PHONE_NUMBER = config("MY_PHONE_NUMBER")
MY_TWILIO_NUMBER = config("MY_TWILIO_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

call = client.calls.create(
    twiml="<Response><Say>What's up, Bro?</Say></Response>",
    to=MY_PHONE_NUMBER,
    from_=MY_TWILIO_NUMBER
)

print(call.sid)