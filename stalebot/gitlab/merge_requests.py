import gitlab
import os
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from dateutil.parser import parse

gl = gitlab.Gitlab("https://gitlab.com", private_token=os.environ["GITLAB_TOKEN"])
gl.auth()

project_id = os.environ["PROJECT_ID"]
project = gl.projects.get(project_id)


def find_stale():
    mrs = project.mergerequests.list(state="opened", order_by="updated_at")

    # filter MRs based on time since updated_at
    max_age = timedelta(days=30)
    stale_date = datetime.now(timezone.utc) - max_age
    mr = [mr for mr in mrs if parse(mr.updated_at) < stale_date][-1]

    return {
        "project_id": project.id,
        "project_name": project.name,
        "iid": mr.iid,
        "author": mr.author["name"],
        "title": mr.title,
        "description": mr.description,
        "updated_at": parse(mr.updated_at).strftime("%b %d %Y"),
    }


def close(mr_id):
    mr = project.mergerequests.get(mr_id)
    mr.state_event = "close"
    mr.save()
