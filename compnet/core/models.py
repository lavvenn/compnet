__all__ = ()

from django.db import models
from django.forms import ValidationError

from core.utils import normalize_name


class NormalizedNameMixin:

    def clean(self):
        super().clean()
        if hasattr(self, 'name'):
            normalized = normalize_name(self.name)
            self.normalized_name = normalized
            qs = self.__class__.objects.filter(normalized_name=normalized)
            if self.pk:
                qs = qs.exclude(pk=self.pk)

            if qs.exists():
                raise ValidationError('Объект с таким именем уже существует!')
        else:
            raise ValidationError('Модель должна иметь поле name')
