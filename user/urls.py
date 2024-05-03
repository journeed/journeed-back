from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "user"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("reset/password/", views.ResetPasswordView.as_view(), name="reset_password"),
    path("change/password/", views.ChangePasswordView.as_view(), name="change_password"),
    path("reset/password/check/<uuid>/", views.ResetPasswordCheckView.as_view(), name="reset_password_check"),
    path("reset/password/complete/<uuid>/", views.ResetPasswordCompleteView.as_view(), name="reset_password_complete"),

    path("profile/", views.ProfileView.as_view(), name="profile")
]
