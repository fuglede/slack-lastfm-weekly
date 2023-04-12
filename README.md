# Slack Last.fm weekly message

A simple script for posting a weekly message to a Slack channel with the most popular artists for a given set of users.


## Usage

First, create [an incoming webhook](https://api.slack.com/legacy/custom-integrations/messaging/webhooks) for your Slack channel, and [create an API account](https://www.last.fm/api/account/create) for your Last.fm user. Take note of the Slack webhook URL and the Last.fm API key. Then, to post a message to Slack for the Last.fm users `user1`, `user2`, and `user3`, run

```
python weekly.py https://hooks.slack.com/services/your/slack/webhook lastfm-api-key user1 user2 user3
```