from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)

from core.forms import BootstrapFormMixin
from users.models import User


class SingUpForm(BootstrapFormMixin, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError('Пароли не совпадают')

        return cleaned_data['password1']


class UserForm(BootstrapFormMixin, UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['email', 'first_name']
        exclude = ['password']


class LoginForm(BootstrapFormMixin, AuthenticationForm):
    username = forms.CharField(label='Email или имя пользователя')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )
            if self.user_cache is None:
                raise forms.ValidationError(
                    'Неверное имя пользователя или пароль',
                )

            if not self.user_cache.is_active:
                raise forms.ValidationError('Пользователь не активен')

        return self.cleaned_data


class ChangePasswordForm(BootstrapFormMixin, PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']