from django.conf import settings
from django.contrib.auth import views
from django.urls import path

import users.forms
import users.views

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(
            template_name='users/login.html',
            form_class=users.forms.LoginForm,
        ),
        name='login',
    ),
    path(
        'logout/',
        views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout',
    ),
    path(
        'password_change/',
        views.PasswordChangeView.as_view(
            template_name='users/password_change.html',
            form_class=users.forms.ChangePasswordForm,
        ),
        name='change_password',
    ),
    path(
        'password/done/',
        views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html',
        ),
        name='change_password_done',
    ),
    path(
        'password/',
        views.PasswordResetView.as_view(
            template_name='users/password_reset.html',
            from_email=settings.MAIL,
            html_email_template_name='users/password_reset_email.html',
        ),
        name='password_reset',
    ),
    path(
        'password_reset/done/',
        views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'password_reset/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    path(
        'password_reset/complete/',
        views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    path(
        'signup/',
        users.views.RegisterView.as_view(),
        name='signup',
    ),
    path(
        'activate/<str:username>/',
        users.views.ActivateUserView.as_view(),
        name='activate_user',
    ),
    path(
        'activate_after_fail_attempts/<str:username>/',
        users.views.ActivateUserAfterFailAttemptsView.as_view(),
        name='activate_user_after_fail_attempts',
    ),
]