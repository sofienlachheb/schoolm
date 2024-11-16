# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False, label="مدير")
    is_teacher = forms.BooleanField(required=False, label="مدرس")
    is_student = forms.BooleanField(required=False, label="طالب")
    is_parent = forms.BooleanField(required=False, label="ولي أمر")
    username = forms.CharField(
        label='اسم المستخدم',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        label='كلمة السر',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
               
            }
        )
    )
    password2 = forms.CharField(
        label='تأكيد كلمة السر',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        label='البريد الإلكتروني',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 
                  'email', 
                  'password1',
                  'password2',
                  'is_admin',
                  'is_teacher',
                  'is_student',
                  'is_parent']
    def clean(self):
            cleaned_data = super().clean()
            password1 = cleaned_data.get("password1")
            password2 = cleaned_data.get("password2")
            if password1 != password2:
               self.add_error('password2', "هناك خطأ كلمات السر غير متطابقة")
class LoginForm(forms.Form):
     username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
     password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )