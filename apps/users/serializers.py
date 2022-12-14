from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

from .models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ('user',)


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at',
            'updated_at', 'profile'
        )
        read_only_field = (
            'id', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at', 'updated_at'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic()
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user

class AddAvatarSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)