from django.urls import path
from .views import RegisterView, VerifyEmail
from django.urls import re_path


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
]

