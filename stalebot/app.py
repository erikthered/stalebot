import os
from flask import Flask, request, session
from stalebot.gitlab import merge_requests
from stalebot.twilio import sms
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

recipient_number = os.environ["RECIPIENT_PHONE_NUMBER"]
pending_mrs = {}


@app.route("/")
def hello():
    return "Welcome to StaleBot"


@app.route("/trigger")
def trigger():

    mr = merge_requests.find_stale()

    message = f"""
MR#{mr['iid']} for project {mr['project_name']} is stale
Opened by: {mr['author']}
Title: {mr['title']}
Description: {mr['description']}
Last Updated: {mr['updated_at']}
Respond with '1' to close.
    """

    sms.send_stale_sms(message, recipient_number)

    # associate MR id with phone number form use in response
    pending_mrs[recipient_number] = mr["iid"]

    return "Triggered!"


@app.route("/respond", methods=["GET", "POST"])
def response():
    sender = request.values.get("From")
    body = request.values.get("Body", None)
    resp_msg = MessagingResponse()

    if body != "1":
        resp_msg.message("I don't understand, sorry.")
        return str(resp_msg)

    if sender not in pending_mrs:
        resp_msg.message("I don't know you, sorry.")
        return str(resp_msg)

    mr_id = pending_mrs.get(sender, None)

    if mr_id is None:
        resp_msg.message("There's no merge request currently awaiting review.")
        return str(resp_msg)

    # close MR
    merge_requests.close(mr_id)

    pending_mrs[recipient_number] = None

    resp_msg.message(f"Closed MR#{mr_id}")

    return str(resp_msg)
