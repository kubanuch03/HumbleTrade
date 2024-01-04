from decouple import config

from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate

from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True, required=True)
    full_name = serializers.CharField(required=True)

    class Meta:
        model = Client
        fields = (
            "id",
            "email",
            "username",
            "full_name",
            "phone_number",
            "password",
            "password2",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Пароль не совпадает, попробуйте еще раз"}
            )
        return attrs

    def create(self, validated_data):
        client = Client.objects.create_client(
            email=validated_data["email"],
            username=validated_data.get("username", ""),
            phone_number=validated_data.get("phone_number", ""),
            full_name=validated_data.get("full_name", ""),
            password=validated_data["password"],
            token_auth=get_random_string(64),
        )

        current_site = get_current_site(self.context["request"])
        domain = current_site.domain
        protocol = "https" if self.context["request"].is_secure() else "http"
        confirmation_link = reverse(
            "clients:confirm_email", kwargs={"token": client.token_auth}
        )

        subject = "Подтверждение почты"
        message = (
            f"Подтвердите почту по ссылке: \n\n{protocol}://{domain}{confirmation_link}"
        )
        from_email = config("EMAIL_HOST_USER")
        to_email = validated_data["email"]
        send_mail(subject, message, from_email, [to_email], fail_silently=False)
        make_password(validated_data["password"])

        return client


class LoginClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Client
        fields = ("email", "password")
