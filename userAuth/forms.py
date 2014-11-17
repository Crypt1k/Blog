from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class RegisterForm(ModelForm):
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password (again)",
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_('The two password fields didn\'t match'))
        return password2
