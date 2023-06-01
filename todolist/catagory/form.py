from django import forms
from .models import *

class CatagoryForm(forms.ModelForm):
    class Meta:
        model=Catagory
        fields='__all__'