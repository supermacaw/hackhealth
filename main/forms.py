from django import forms
from main.models import *




class EmailRegisterForm(forms.Form):
    email = forms.EmailField(label="Email")
    pw1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    pw2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
