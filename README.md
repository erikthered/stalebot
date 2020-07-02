# GitLab Stale MR Bot

This is an experiment that allows you to close stale GitLab merge requests via
SMS using Twilio.

Currently "stale" MRs are ones that haven't been updated in 30 days. This value is currently hardcoded but will be configurable in the future.

The app will currently query the GitLab API for stale MRs and send you one that is a candidate for closing. You can reply with '1' to close or '2' to skip (noted in the SMS message).

This interaction is currently triggered via the `/trigger` HTTP endpoint but in the future support may be added for executing this behavior on a trigger and/or chaining off of a 'skip' event.

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

You'll need to configure an SMS callback URL in Twilio in order to handle SMS responses. I'd highly recommend [ngrok](https://ngrok.com/) for local development/usage.

## To-Do's

- [x] Handle SMS replies
  - [x] Handle close response
  - [x] Handle skip response
  - [ ] Accept comment for closing a MR
- [ ] Support multiple phone numbers
- [ ] Support multiple GitLab projects
- [ ] Support GitLab groups
- [ ] Deployment configs
- [ ] Cron/Scheduled run