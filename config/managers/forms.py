from .models import Subjects, SiteSetting,UploadedFile
from django import forms

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['subjectName', 'photo']

class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = ['school_name', 'school_logo', 'favicon']

class UserUploadForm(forms.Form):
    excel_file = forms.FileField(label='Select an Excel File')