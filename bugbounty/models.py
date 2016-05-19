import enumfields
from django.db import models
from django.utils import timezone

class ReportType(enumfields.Enum):
    AUTH_FAIL = "auth_fail"
    CSRF = "csrf"
    XSS = "xss"
    CRYPTO = "crypto"
    DOS = "dos"
    DESIGN = "design"
    INFORMATION_DISCLOSURE = "information_disclosure"
    MISSING_BEST_PRACTICE = "missing_best_practice"
    PRIVESC = "privesc"
    RCE = "rce"
    SQLI = "sqli"
    CLICKJACKING = "clickjacking"
    REDIRECT = "open_redirect"
    OTHER = "other"

    class Labels:
        AUTH_FAIL = "Authentication bypass/failure"
        CSRF = "Cross-Site Request Forgery (CSRF)"
        XSS = "Cross-Site Scripting (XSS)"
        CRYPTO = "Cryptographic issue"
        DOS = "Denial of Service"
        DESIGN = "Design Issue"
        INFORMATION_DISCLOSURE = "Information Disclosure"
        MISSING_BEST_PRACTICE = "Missing Best Practice"
        PRIVESC = "Privilege Escalation"
        RCE = "Remote Code Execution"
        SQLI = "SQL Injection"
        CLICKJACKING = "Clickjacking"
        REDIRECT = "Open Redirect"
        OTHER = "Other"

class ReportStatus(enumfields.Enum):
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    WAITING = 'waiting'
    RESOLVED = 'resolved'
    INVALID = 'invalid'

class Report(models.Model):
    reporter_name = models.TextField()
    reporter_email = models.EmailField()

    type = enumfields.EnumField(ReportType, max_length=200)
    title = models.TextField()
    details = models.TextField()
    status = enumfields.EnumField(ReportStatus, max_length=200, default=ReportStatus.NEW)

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.date_updated = timezone.now()
        super().save(*args, **kwargs)

    def __unicode__(self):
        return self.title

