import django.test
from django.core import mail
from django.core.urlresolvers import reverse
from bugbounty.models import Report, Target

class SimpleViewTests(django.test.SimpleTestCase):
    """Tests for views that don't require a DB."""

    def test_index(self):
        r = self.client.get(reverse('bounty-index'))
        assert r.status_code == 200

    def test_thanks(self):
        r = self.client.get(reverse('bounty-thanks'))
        assert r.status_code == 200

    def test_project_instructions(self):
        r = self.client.get(reverse('bounty-project-instructions'))
        assert r.status_code == 200

class ModelViewTests(django.test.TestCase):
    """Tests for views that do require a DB."""

    def setUp(self):
        self.target = Target.objects.create(name="Test Target", is_active=True)
        self.target.owners.create(username='john', email='lennon@beatles.com')

    def test_submit(self):
        data = {
            "reporter_name": "George Harrison",
            "reporter_email": "george@beatles.com",
            "target": self.target.id,
            "type": "xss",
            "title": "This is my bug report.",
            "details": "It isn't very long."
        }
        r = self.client.post(reverse('bounty-submit'), data=data)
        self.assertRedirects(r, reverse('bounty-thanks'))

        report = Report.objects.get(reporter_email=data['reporter_email'])
        assert report.title == data['title']

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == '[Bug Bounty] New report against Test Target'
        assert mail.outbox[0].to == [o.email for o in self.target.owners.all()]
