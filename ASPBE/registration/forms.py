from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User=get_user_model()

class UserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'registration__input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'registration__input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'registration__input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'registration__input'}))
    account_type = forms.ChoiceField(
        choices=User.account_type.field.choices,
        widget=forms.Select(attrs={'class': 'form-input'})
    )

    field_order = ['username',  'email', 'password1', 'password2', 'account_type']

    class Meta(UserCreationForm):
        model = User
        fields = {'username',  'email', 'password1', 'password2', 'account_type'}
        widgets = {
            'username' : forms.TextInput(attrs={'class':'registration__input'}),
            'email': forms.EmailInput(attrs={'class':'registration__input'}),
            'password1' : forms.PasswordInput(attrs={'class':'registration__input'}),
            'password2' : forms.PasswordInput(attrs={'class':'registration__input'}),
            'account_type': forms.Select(attrs={'class': 'form-input'})
        }


