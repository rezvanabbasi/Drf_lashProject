from django.contrib.auth import login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from apps.users.models import UserType, Profile
from apps.users.serializers import (
    UserTypeSerializer,
    RegisterSerializer,
    LoginSerializer,
    ForgetPasswordSerializer,
    ConfirmVerificationCode
)

import random
from config.tasks import kave_negar_token_send
from apps.users.models import OtpCode


class SetTypeApiView(APIView):

    def post(self, request):
        serializer = UserTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(request.data)
        return Response(data={'User Type created!'}, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        query_set = UserType.objects.all()

        return Response(
            data=UserTypeSerializer(query_set, many=True).data,
            status=status.HTTP_200_OK
        )


class RegisterApiView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()

        return Response(
            data=token,
            status=status.HTTP_201_CREATED
        )


class LoginApiView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)

        return Response(
            data='Logged in',
            status=status.HTTP_200_OK
        )


class ForgetPasswordApiView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ForgetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        random_code = random.randint(1000, 9999)
        kave_negar_token_send.delay(
            receptor=request.data['mobile'],
            token=random_code
        )
        OtpCode.objects.create(
            mobile=request.data['mobile'],
            code=random_code
        )

        confirm_code_link = request.build_absolute_uri(
            reverse(f'confirm-code')
        )
        return Response(
            data={'Confirmation code sent! Click on link', confirm_code_link},
            status=status.HTTP_200_OK
        )


class ConfirmPasswordApiView(APIView):

    def post(self, request):
        serializer = ConfirmVerificationCode(data=request.data)
        serializer.is_valid(raise_exception=True)

        verification_code = request.data['code']

        if verification_code:
            mobile = OtpCode.objects.get(code=verification_code)
            profile = Profile.objects.get(phone_number=mobile)
            if request.data['password'] == request.data['confirm_password']:
                profile.change_password(request.data['password'])
                profile.save()
            else:
                return Response(
                    data={'Password and confirm password are not equal'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                data={'Submitted code is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(data={'Password changed!'}, status=status.HTTP_200_OK)
