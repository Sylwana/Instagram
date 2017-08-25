from .models import User
from django import forms
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user=None

    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data['login']
        password = cleaned_data['password']
        self.user = authenticate(username=login, password=password)
        if self.user is None:
            raise forms.ValidationError('Wrong user or password')
        # cleaned_data['user']=self.user
        return cleaned_data