from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token

from apps.users.models import Profile, UserType


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        profile = Profile(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            username=validated_data['username'],
            password=validated_data['password'],
            full_name=validated_data['full_name'],
            address=validated_data['address'],
            birth_date=validated_data['birth_date'],
        )
        type_id = validated_data['user_type']
        type = UserType.objects.get(title__exact=type_id)
        profile.user_type = type

        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password']

        )
        profile.user = user

        token = Token.objects.create(user=user).key

        user.save()
        profile.save()

        return token


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label='Username', write_only=True)
    password = serializers.CharField(label='Password', write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            profile = Profile.objects.get(
                username__exact=username,
                password__exact=password
            )
            if not profile:
                raise serializers.ValidationError(
                    'wrong username or password!',
                    code='authorization'
                )
        else:
            raise serializers.ValidationError(
                'Username and password are required!'
            )
        user = profile.user
        data['user'] = user

        return user


class ForgetPasswordSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)


class ConfirmVerificationCode(serializers.Serializer):
    code = serializers.IntegerField()
    password = serializers.CharField(max_length=8)
    confirm_password = serializers.CharField(max_length=8)
