from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.db import transaction
from django import forms
from django.forms import TextInput, PasswordInput

from authentication.models import MyUser


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = MyUser.objects.get(email=email)
        except MyUser.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already taken. Please try another email.')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=120,
                                 widget=TextInput(attrs={'class': 'form-control', 'id': 'first_name', 'type': 'text',
                                                         'required data-validation-required-message': 'Please enter your first name.'}))
    last_name = forms.CharField(max_length=120,
                                widget=TextInput(attrs={'class': 'form-control', 'id': 'last_name', 'type': 'text',
                                                        'required data-validation-required-message': 'Please enter your last name.'}))
    email = forms.EmailField(max_length=120,
                             widget=TextInput(attrs={'class': 'form-control', 'id': 'email', 'type': 'email',
                                                     'required data-validation-required-message': 'Please enter your email.'}))
    password1 = forms.CharField(max_length=500,
                                widget=TextInput(attrs={'class': 'form-control', 'id': 'password', 'type': 'password',
                                                        'required data-validation-required-message': 'Please enter your password.'}))
    password2 = forms.CharField(max_length=500,
                                widget=TextInput(
                                    attrs={'class': 'form-control', 'id': 'confirm-password', 'type': 'password',
                                           'required data-validation-required-message': 'Please enter your confirm-password.'}))

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=TextInput(attrs={'class': 'form-control',
                                                    'id': 'email',
                                                    }))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                           'id': 'password',
                                                           }))
