from django import forms
from django.contrib.auth.models import *
from .models import *
#gui form --->class inhertitancre Form ,ModelForm
class RegistrationAdminform(forms.Form):
    #email
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'style':'color:red'
    }))
    #username
    username=forms.CharField()
    #password
    passworrd=forms.CharField(label='Password',widget=forms.PasswordInput(

    ),max_length=12,required=False)

class RegistrationAdminformModel(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=MyUser
        #fields='__all__'#['email','username']#'__all__'
        exclude=['password']