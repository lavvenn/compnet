import re

import django.contrib.auth.models
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now


class UserManager(django.contrib.auth.models.BaseUserManager):

    def normalize_email(self, email):
        if not email or '@' not in email:
            return email

        email = super().normalize_email(email)
        email = email.lower()
        local_part, domain = email.split('@')

        local_part = local_part.split('+')[0]

        if domain in ['yandex.ru', 'ya.ru']:
            domain = 'yandex.ru'
            local_part = local_part.replace('.', '-')
        elif domain == 'gmail.com':
            local_part = local_part.replace('.', '')

        local_part = re.sub(r'\+.*', '', local_part)
        return f'{local_part}@{domain}'

    def get_queryset(self):
        return super().get_queryset().select_related('profile')

    def active(self):
        return self.get_queryset().filter(is_active=True)

    def by_mail(self, email):
        return self.get_queryset().get(email=email)


class User(django.contrib.auth.models.User):

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.email = User.objects.normalize_email(self.email)
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username