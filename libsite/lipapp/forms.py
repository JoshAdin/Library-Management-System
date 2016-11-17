from django import forms
from django.contrib.auth.models import User
from lipapp.models import Suggestion


class SuggestionForm(forms.ModelForm):
    TYPE_CHOICES = (
        (1, 'Book'),
        (2, 'DVD'),
        (3, 'Other'),
    )

    type = forms.IntegerField(widget=forms.RadioSelect(choices=TYPE_CHOICES))
    title = forms.CharField(max_length=100, required=True)
    cost = forms.IntegerField(label='Estimated Cost In Dollars')

    class Meta:
        model = Suggestion
        fields = ['title', 'type', 'pubyr', 'cost', 'comments']
        # widgets={
        # 'type' = forms.RadioSelect
        # }


class SearchlibForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    author = forms.CharField(max_length=100, required=False)


class LoginForm(forms.ModelForm):

    password = forms.CharField(required=True, widget=forms.PasswordInput)
    username = forms.CharField(error_messages={'required': 'This field is required'})

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    username = forms.CharField(error_messages={'required': 'This field is required'})
    password2 = forms.CharField(required=True,label="Repeat Password", widget=forms.PasswordInput)
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {'email': forms.EmailInput,
                   'password': forms.PasswordInput}


