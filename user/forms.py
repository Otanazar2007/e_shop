from calendar import month

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class BankCartForm(forms.Form):
    number = forms.IntegerField()
    name = forms.CharField(max_length=100)
    time = forms.CharField(max_length=5)
    cvv = forms.IntegerField()

















































