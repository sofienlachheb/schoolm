from django import forms
from .models import ClassGrade, GradeName, Grade

class ClassGradeForm(forms.ModelForm):
    class Meta:
        model = ClassGrade
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ClassGrade name'}),
        }

class GradeNameForm(forms.ModelForm):
    class Meta:
        model = GradeName
        fields = ['class_grade', 'name']
        widgets = {
            'class_grade': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter GradeName'}),
        }

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['grade_name', 'code']
        widgets = {
            'grade_name': forms.Select(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Grade Code'}),
        }
