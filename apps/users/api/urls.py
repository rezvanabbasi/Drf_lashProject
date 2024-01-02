from django.urls import path

from apps.users.api.api import (
    SetTypeApiView,
    RegisterApiView,
    LoginApiView,
    ForgetPasswordApiView,
    ConfirmPasswordApiView
)

app_name = "users"

urlpatterns = [
    path('type/', SetTypeApiView.as_view(), name='type'),
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('forget-password/', ForgetPasswordApiView.as_view(), name='forget-password'),
    path('confirm-password/', ConfirmPasswordApiView.as_view(), name='confirm-password'),
]
