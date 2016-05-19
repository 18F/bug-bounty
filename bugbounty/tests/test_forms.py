from bugbounty.forms import ReportForm

def test_report_form():
    data = {
        "reporter_name": "George Harrison",
        "reporter_email": "george@beatles.com",
        "type": "xss",
        "title": "This is my bug report.",
        "details": "It isn't very long."
    }
    form = ReportForm(data)
    assert form.is_valid(), form.errors