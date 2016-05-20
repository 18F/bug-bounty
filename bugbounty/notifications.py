"""
Utilities to send notifications about a new report.

Right now sends notifications about Slack (if Slack's configured). Abstracted
out so that it'll be less coupled to the form/model, and so that if we want to
support different notification methods (email, etc) it'll be easier to do so.
"""

import json
import requests
from django.core.urlresolvers import reverse
from django.conf import settings

def send_report_notification(request, report):
    if getattr(settings, 'SLACK_INCOMING_WEBHOOK', None) is not None and report.target.slack_channel:
        report_link = request.build_absolute_uri(reverse('admin:bugbounty_report_change', args=(report.id,)))
        report_text = "New report against {}\n<{}|Click here for details>".format(report.target.name, report_link)
        payload = {
            "text": report_text,
            "username": "Bug Bounty Bot",
            "icon_emoji": ":bug:",
            "channel": report.target.slack_channel
        }
        requests.post(
            settings.SLACK_INCOMING_WEBHOOK,
            data = json.dumps(payload),
            headers = {'Content-type': 'application/json'}
        )
