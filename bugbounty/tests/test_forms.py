import pytest
from bugbounty.forms import ReportForm
from bugbounty.models import Target

@pytest.mark.django_db
def test_report_form():
    t = Target.objects.create(name="Test Target")
    data = {
        "reporter_name": "George Harrison",
        "reporter_email": "george@beatles.com",
        "target": t.id,
        "type": "xss",
        "title": "This is my bug report.",
        "details": "It isn't very long."
    }
    form = ReportForm(data)
    assert form.is_valid(), form.errors