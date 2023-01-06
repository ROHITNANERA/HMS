from string import digits
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email','password1','password2']



class HostelForm(forms.ModelForm):
    class Meta:
        model=Hostel
        fields = '__all__'
        exclude = ['h_user']
