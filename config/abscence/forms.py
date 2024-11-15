from django import forms
from .models import Abscence

class AbscenceForm(forms.ModelForm):
    class Meta:
        model = Abscence
        fields ='__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
