from .models import Subjects, SiteSetting
from django import forms

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['subjectName', 'photo']

class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = ['school_name', 'school_logo', 'favicon']
