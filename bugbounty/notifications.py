"""
Utilities to send notifications about a new report.

Right now sends notifications about Slack (if Slack's configured). Abstracted
out so that it'll be less coupled to the form/model, and so that if we want to
support different notification methods (email, etc) it'll be easier to do so.
"""

import json
import requests
from django.conf import settings

def send_report_notification(report):
    if hasattr(settings, 'SLACK_INCOMING_WEBHOOK') and report.target.channel:
        report_link = "https://example.com/fixme"
        report_text = "New report against {}\n<{}|Click here for details>".format(report.target.name, report_link) 
        payload = {
            "text": report_text,
            "username": "Bug Bounty Bot",
            "icon_emoji": ":bug:",
            "channel": report.target.channel 
        }
        requests.post(
            settings.SLACK_INCOMING_WEBHOOK, 
            data = json.dumps(payload), 
            headers = {'Content-type': 'application/json'}
        )