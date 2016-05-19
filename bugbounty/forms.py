import floppyforms.__future__ as forms
from .models import Report, Target
from django.core.mail import send_mail
from django import template 

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reporter_name', 'reporter_email', 'target', 'type', 'title', 'details']
        widgets = {
            'reporter_name': forms.TextInput(),
            'title': forms.TextInput(),
        }
        labels = {
            'reporter_name': 'Your name',
            'reporter_email': 'Your email',
        }
        help_texts = {
            'reporter_email': "We'll only use this email to contact you about your report. We hate spam as much as you do."
        }

    # Only allow active targets to be reported against
    target = forms.ModelChoiceField(queryset=Target.objects.filter(is_active=True)) 

    def save(self, *args, **kwargs):
        report = super().save(*args, **kwargs)
        
        t = template.loader.get_template('bugbounty/new-report-email.txt')
        c = template.Context({'report': report})
        mail_message = t.render(c)

        send_mail(
            subject = "[Bug Bounty] New report against {}".format(report.target.name),
            message = mail_message,
            recipient_list = [o.email for o in report.target.owners.all()],

            # FIXME - I'm not sure if this actually does what I want. 
            # Need to verify that it does and that it works. 
            from_email = report.reporter_email
        )

        return report