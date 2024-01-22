from django import forms
from django.forms import ModelForm
from .models import Member, UserProfile


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'password']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'password']




from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    what = forms.EmailField()
    


    class Meta:
        model = UserProfile 
        fields = ['username','what', 'password1', 'password2']

