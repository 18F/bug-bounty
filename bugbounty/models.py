import enum
import enumfields
from django.db import models
from django.utils import timezone

class ReportType(enum.Enum):
    auth_fail = "Authentication bypass/failure"
    csrf = "Cross-Site Request Forgery (CSRF)"
    xss = "Cross-Site Scripting (XSS)"
    crypto = "Cryptographic issue"
    dos = "Denial of Service"
    design = "Design Issue"
    information_disclosure = "Information Disclosure"
    missing_best_practice = "Missing Best Practice"
    privesc = "Privilege Escalation"
    rce = "Remote Code Execution"
    sqli = "SQL Injection"
    clickjacking = "Clickjacking"
    redirect = "Open Redirect"
    other = "Other"

class ReportStatus(enum.Enum):
    new = 'new'
    in_progress = 'in progress'
    waiting = 'waiting on reporter'
    resolved = 'resolved'
    invalid = 'invalid'

class Report(models.Model):
    reporter_name = models.TextField()
    reporter_email = models.EmailField()

    type = enumfields.EnumField(ReportType, max_length=200)
    title = models.TextField()
    details = models.TextField()
    status = enumfields.EnumField(ReportStatus, max_length=200, default=ReportStatus.new)

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.date_updated = timezone.now()
        super().save(*args, **kwargs)

    def __unicode__(self):
        return self.title

