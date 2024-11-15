from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ('weeks','sceance','behavior',  'comment')
        widgets = {
            
            'created': forms.DateInput(attrs={'type': 'date'}),
        }