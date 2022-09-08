from string import digits
from django import forms
from .models import *


#create froms here
class HAdminForm(forms.ModelForm):
    class Meta:
        model = HAdmin
        fields = '__all__'



class LoginForm(forms.Form):
    email = forms.EmailField(max_length=40)
    psw = forms.CharField(widget=forms.PasswordInput())

class HostelForm(forms.ModelForm):
    class Meta:
        model=Hostel
        fields = '__all__'
