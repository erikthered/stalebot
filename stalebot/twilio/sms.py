import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
outgoing_number = os.environ["TWILIO_OUTGOING_NUMBER"]
recipient_number = os.environ["RECIPIENT_PHONE_NUMBER"]

twilio_client = Client(account_sid, auth_token)


def send_stale_sms(message):
    message = twilio_client.messages.create(
        body=message, from_=outgoing_number, to=recipient_number
    )

