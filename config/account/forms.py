# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    is_admin = forms.BooleanField(
        required=False,
        label="مدير",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    is_teacher = forms.BooleanField(
        required=False,
        label="مدرس",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    is_student = forms.BooleanField(
        required=False,
        label="طالب",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    is_parent = forms.BooleanField(
        required=False,
        label="ولي أمر",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    username = forms.CharField(
        label="اسم المستخدم",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "أدخل اسم المستخدم"})
    )
    email = forms.CharField(
        label="البريد الإلكتروني",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "أدخل بريدك الإلكتروني"})
    )
    password1 = forms.CharField(
        label="كلمة السر",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "أدخل كلمة السر"})
    )
    password2 = forms.CharField(
        label="تأكيد كلمة السر",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "تأكيد كلمة السر"})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_admin', 'is_teacher', 'is_student', 'is_parent']
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