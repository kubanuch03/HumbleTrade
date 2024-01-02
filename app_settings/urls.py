from django.urls import path
from .views import *


app_name = "profile"
urlpatterns = [
    path('profile/', ClientProfileView.as_view(), name='client_profile'),
     path(
        "reset-password/client/",
        RequestPasswordResetView.as_view(),
        name="reset-password",
    ),
    path(
        "reset-password-confirm/client/<str:uidb64>/<str:token>/",
        ResetPasswordConfirmView.as_view(),
        name="reset-password-confirm",
    ),
]