import gitlab
import os
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from dateutil.parser import parse
from pprint import pprint
from twilio.rest import Client

gl = gitlab.Gitlab("https://gitlab.com", private_token=os.environ["GITLAB_TOKEN"])
gl.auth()

current_user = gl.user

project_id = os.environ["PROJECT_ID"]
project = gl.projects.get(project_id)
mrs = project.mergerequests.list(state="opened", order_by="updated_at")

# filter MRs based on time since updated_at
max_age = timedelta(days=30)
stale_date = datetime.now(timezone.utc) - max_age
stale_mrs = [mr for mr in mrs if parse(mr.updated_at) < stale_date]

for mr in stale_mrs:
    print(
        f"""MR#{mr.iid} for project {project.name} is stale
Opened by: {mr.author['name']}
Title: {mr.title}
Description: {mr.description}
Last Updated: {parse(mr.updated_at).strftime("%b %d %Y")}
        """
    )

# TODO move twilio stuff to a separate module

# account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]

# twilio_client = Client(account_sid, auth_token)

# TODO send SMS with oldest MR details

# message = twilio_client.messages.create(
#     body="Test from Twilio", from_="", to=""
# )

# print(message.sid)

# TODO handle response (via Lambda/FAAS or HTTP endpoint)
