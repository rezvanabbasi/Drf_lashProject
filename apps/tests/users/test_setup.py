from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase

from apps.users.models import User, Profile, UserType, OtpCode


class SetupTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        return super().setUpTestData

    def setUp(self):
        self.factory = APIRequestFactory()
        self.type_url = reverse("type")
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.forget_password_url = reverse("forget-password")
        self.confirm_password_url = reverse("confirm-password")

        self.credentials = {
            "id": 1,
            "email": "test@test.com",
            "username": "test",
            "full_name": "test profile",
            "phone_number": "12345678910",
            "password": "123456",
        }

        # create user
        self.user = User.objects.create_user(
            username=self.credentials["username"],
            password=self.credentials["password"]
        )

        # create user type
        self.user_type = UserType.objects.create(title='مربی', description='test')

        # create profile
        self.profile = Profile.objects.create(**self.credentials)
        self.profile.user = self.user
        self.profile.user_type = self.user_type
        self.profile.save()

        self.token = Token.objects.create(user_id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        # set user into every request
        self.client.user = self.profile.user

        # create otp code
        self.otp_code = OtpCode.objects.create(
            mobile=self.credentials["phone_number"],
            code=1234
        )

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        print("finished tests of users app")
        return super().tearDownClass()
