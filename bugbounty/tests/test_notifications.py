import pytest
import httpretty
from bugbounty import notifications
from bugbounty.models import Report, ReportType, Target

@httpretty.activate
@pytest.mark.django_db
def test_slack_notification(settings, rf):
    target = Target.objects.create(name="Test Target", is_active=True, slack_channel='#test')
    report = Report.objects.create(
        reporter_name = "George Harrison",
        reporter_email = "george@beatles.com",
        type = ReportType.XSS,
        title = "Title",
        details = "Details",
        target = target,
    )
    settings.SLACK_INCOMING_WEBHOOK = 'https://example.com/web/hook'
    request = rf.get('/submit/')
    httpretty.register_uri(httpretty.POST, settings.SLACK_INCOMING_WEBHOOK)
    notifications.send_report_notification(request, report)

    request = httpretty.last_request()
    assert request.parsed_body['channel'] == target.slack_channel
