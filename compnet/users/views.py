__all__ = ()

from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView, FormView, ListView, TemplateView

from users.forms import SingUpForm, UserForm
from users.models import User


class RegisterView(FormView):
    template_name = 'users/signup.html'
    form_class = SingUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = settings.DEFAULT_USER_IS_ACTIVE
        user.save()
        messages.success(
            self.request,
            'Профиль успешно создан, можете войти в него.',
        )
        return super().form_valid(form)


class ActivateUserView(View):
    template_name = 'users/activation_result.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        now = timezone.now()

        if not user.is_active and (now - user.date_joined) <= timedelta(
            hours=12,
        ):
            user.is_active = True
            user.save()
            message = 'Ваш аккаунт успешно активирован.'
        else:
            message = 'Срок активации истёк или пользователь уже активен.'

        return render(request, self.template_name, {'message': message})


class ActivateUserAfterFailAttemptsView(View):
    template_name = 'users/activation_result.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        now = timezone.now()

        if not user.is_active and (
            now - user.profile.last_attempt
        ) <= timedelta(hours=168):
            user.is_active = True
            user.save()
            message = 'Ваш аккаунт успешно активирован.'
        else:
            message = 'Срок активации истёк или пользователь уже активен.'

        return render(request, self.template_name, {'message': message})


class UsersListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.active()
