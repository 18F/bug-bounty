import pytest
from bugbounty.models import Report, ReportType, ReportStatus

@pytest.mark.django_db
def test_report_save_updates_date_updated():
    r = Report.objects.create(
        reporter_name = "George Harrison",
        reporter_email = "george@beatles.com",
        type = ReportType.XSS,
        title = "Title",
        details = "Details",
    )

    # To avoid monkeypatching date, just check that the date increased. Close enough.
    old_update_date = r.date_updated
    r.status = ReportStatus.IN_PROGRESS
    r.save()
    assert r.date_updated > old_update_date
