from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import logout_view

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("home/", views.home, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path("logout/", logout_view, name="logout"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html')),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html')),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html')),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete")
    

]