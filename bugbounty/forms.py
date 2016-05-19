import floppyforms.__future__ as forms
from .models import Report

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
            'reporter_email': "We'll only use this email to contact you about your submission. We hate spam as much as you do."
        }