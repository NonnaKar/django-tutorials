from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

app_name ="accounts"

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('change-password/', views.change_password, name='change-password'),
    path('reset_password/', PasswordResetView.as_view
    (
        template_name='accounts/reset_password.html',
        email_template_name='accounts/reset_password_email.html',
        subject_template_name = 'accounts/reset_password_subject.txt',
        success_url = reverse_lazy('accounts:reset_password_done')
    ), name='reset_password'),
    path('reset-password/done/', PasswordResetDoneView.as_view
    (
        template_name='accounts/reset_password_done.html'
    ), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
