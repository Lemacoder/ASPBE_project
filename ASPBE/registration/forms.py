from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CreateUserForm(UserCreationForm):
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