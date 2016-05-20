from django import forms
from django.contrib import admin
from .models import Report, Target

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_updated', 'status', 'type')
    ordering = ('-date_updated',)
    list_filter = ('status',)
    search_fields = ('title',)
    readonly_fields = ('reporter_name', 'reporter_email', 'target', 'type', 'title', 'details', 'date_created', 'date_updated')
    fields = readonly_fields + ('status',)

class TargetAdminForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': '50'}),
            'slack_channel': forms.TextInput(attrs={'size': '50'}),
        }

@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    ordering = ('name',)
    list_filter = ('is_active',)
    search_fields = ('name',)
    form = TargetAdminForm
