from flask import Flask
from stalebot.gitlab import merge_requests
from stalebot.twilio import sms

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to StaleBot"


@app.route("/trigger")
def trigger():

    mr = merge_requests.find_stale()

    message = f"""
MR#{mr['number']} for project {mr['project_name']} is stale
Opened by: {mr['author']}
Title: {mr['title']}
Description: {mr['description']}
Last Updated: {mr['updated_at']}
    """

    sms.send_stale_sms(message)

    return "Triggered!"
