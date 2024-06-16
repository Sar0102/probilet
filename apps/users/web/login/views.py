from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView as BaseTokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView as BaseTokenRefreshView

from apps.users.models import User

from .serializers import LoginPayloadSerializer


@extend_schema(
    tags=["auth"],
)
class TokenObtainPairView(BaseTokenObtainPairView):
    serializer_class = LoginPayloadSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self._get_user(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        refresh_token = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh_token),
                "access": str(refresh_token.access_token),
            }
        )

    def _get_user(self, email, password) -> tuple[User] | None:

        user = User.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError(
                {"username": "User doesn't exist with this email or phone number"}
            )

        if not user.check_password(password):
            raise serializers.ValidationError({"password": "Password is incorrect"})

        if not user.is_active:
            raise serializers.ValidationError(
                {"username": "Your profile is not activated"}
            )

        return user


@extend_schema(
    tags=["auth"],
)
class TokenRefreshView(BaseTokenRefreshView): ...
