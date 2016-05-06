from django import forms
from django.contrib import admin
from .models import Report

class ReportAdminForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'reporter_name': forms.TextInput(attrs={'size': '50'}),
            'title': forms.TextInput(attrs={'size': '50'}),
        }

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_updated', 'status', 'type')
    ordering = ('-date_updated',)
    list_filter = ('status',)
    search_fields = ('title',)
    form = ReportAdminForm