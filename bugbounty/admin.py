from django import forms
from django.contrib import admin
from .models import Report, Target

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

class TargetAdminForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': '50'})
        }

@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    ordering = ('name',)
    list_filter = ('is_active',)
    search_fields = ('name',)
    form = TargetAdminForm
