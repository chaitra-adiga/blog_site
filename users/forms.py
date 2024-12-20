from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model=User # says that to interact with which databse 
        fields=['username','email','password1','password2'] # in the same order the fields are displ.

