import pytest
from bugbounty.forms import ReportForm
from bugbounty.models import Target

@pytest.mark.django_db
def test_report_form():
    t = Target.objects.create(name="Test Target", is_active=True)
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

@pytest.mark.django_db
def test_report_form_only_allows_active_targets():
    t_active = Target.objects.create(name="Active Target", is_active=True)
    t_inactive = Target.objects.create(name="Inactive Target", is_active=False)

    data = {
        "reporter_name": "George Harrison",
        "reporter_email": "george@beatles.com",
        "type": "xss",
        "title": "This is my bug report.",
        "details": "It isn't very long."
    }

    form = ReportForm(dict(data, target=t_active.id))
    assert form.is_valid(), form.errors

    form = ReportForm(dict(data, target=t_inactive.id))
    assert not form.is_valid()
    assert list(form.errors.keys()) == ['target']