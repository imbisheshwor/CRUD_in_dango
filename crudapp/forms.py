from tkinter import Widget
from attr import fields
from django import forms
from crudapp.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields="__all__"
        
        widgets = {
            'uname':forms.TextInput(attrs={'class':'form-control'}),
            'uemail':forms.EmailInput(attrs={'class':'form-control'}),
            'upassword':forms.PasswordInput(attrs={'class':'form-control'}),
        }