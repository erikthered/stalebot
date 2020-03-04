# GitLab Stale MR Bot

This is an experiment that allows you to close stale GitLab merge requests via
SMS using Twilio.

## Required Environment Variables

- GITLAB_TOKEN - A GitLab personal access token
- PROJECT_ID - The numeric project ID of your GitLab project
- TWILIO_ACCOUNT_SID - Your Twilio account SID
- TWILIO_AUTH_TOKEN - Your Twilio app auth token
- TWILIO_OUTGOING_NUMBER - The Twilio phone number to use
- RECIPIENT_PHONE_NUMBER - The phone number you want to receive SMS messages on

## Usage

I've included a `requirements.txt` with the necessary dependencies. I've also included
files for running in VS Code's [remote containers](https://code.visualstudio.com/docs/remote/containers), along with launch configs.

## To-Do's

- [x] Handling SMS replies
- [ ] Support multiple phone numbers
- [ ] Support multiple GitLab projects
- [ ] Support GitLab groups
- [ ] Deployment configs
- [ ] Cron/Scheduled run