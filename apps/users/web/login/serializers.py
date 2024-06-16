from rest_framework import serializers


class LoginPayloadSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
