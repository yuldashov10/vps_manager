from rest_framework import serializers

from users.constants import USER_PASSWORD_MIN_LENGTH
from users.models import User


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "avatar")
        read_only_fields = ("id",)


class UserSerializer(UserShortSerializer):
    class Meta(UserShortSerializer.Meta):
        model = User
        fields = UserShortSerializer.Meta.fields + (
            "email",
            "password",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": USER_PASSWORD_MIN_LENGTH,
            },
        }

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data.get("password"))

        return super().update(instance, validated_data)
