import sys

import requests


_, webhook_url, api_key, *users = sys.argv

slack_message_parts = ["Most listened this week:"]

for user in users:
    res = requests.get(
        f"http://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user={user}&api_key={api_key}&format=json"
    ).json()
    artists = ", ".join(
        f"{artist['name']} ({artist['playcount']})"
        for artist in res["weeklyartistchart"]["artist"][:3]
    )
    slack_message_parts.append(f"{user}: {artists}")

slack_message = "\n".join(slack_message_parts)

print("Sending message:")
print(slack_message)
payload = {"text": slack_message}
requests.post(webhook_url, json=payload)
