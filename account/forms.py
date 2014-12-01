from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class RegisterForm(ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password (again)", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                raise forms.ValidationError(_('The two password fields didn\'t match'))
        return password

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(user.password)
        if commit:
            user.save()
        return user
