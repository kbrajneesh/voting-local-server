from django import forms
from django.contrib.auth.models import User

from .models import Round1 , Round2 , Round3


class Round1Form(forms.ModelForm):

    class Meta:
        model = Round1
        fields = ['con1', 'con2', 'con3', 'con4', 'con5', 'con6', 'con7', 'con8', 'con9', 'con10']

class Round2Form(forms.ModelForm):


    class Meta:
        model = Round2
        fields = ['con1', 'con2', 'con3', 'con4', 'con5', 'con6', 'con7', 'con8', 'con9', 'con10']

class Round3Form(forms.ModelForm):

    class Meta:
        model = Round3
        fields = ['con1', 'con2', 'con3', 'con4', 'con5', 'con6', 'con7', 'con8', 'con9', 'con10']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
