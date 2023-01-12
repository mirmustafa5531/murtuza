from django.core import validators
from django import forms
from .models import user
from.models import showing

class clubregistrations(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name','email','password']
        widgets = {
          'name':forms.TextInput(attrs = {'class':'form-control'}),
          'email':forms.EmailInput(attrs = {'class':'form-control'}),
          'password':forms.PasswordInput(attrs = {'class':'form-control'})          
        }


class selectshowing(forms.ModelForm):
    class Meta:
        model = showing
        fields = ['filmtitle','agerating','duration']
        widgets = {
          'filmtitle':forms.TextInput(attrs = {'class':'form-control'}),
          'agerating':forms.TextInput(attrs = {'class':'form-control'}),
          'duration':forms.TextInput(attrs = {'class':'form-control'})          
        }



