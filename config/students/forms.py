from django import forms
from .models import Student
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('user',
                  'name',
                  'grade',
                  'roll_number'
                  )