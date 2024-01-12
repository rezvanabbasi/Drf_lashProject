from .test_setup import SetupTest


class UserTypeTest(SetupTest):
    def setUp(self):
        self.type_data = {
            "title": "مربی",
            "description": "this is test"
        }
        return super().setUp()

    def test_user_type_create(self):
        response = self.client.post(self.type_url, self.type_data)
        self.assertEquals(response.status_code, 201)


class RegisterTest(SetupTest):
    def setUp(self):
        self.register_data = {
            "email": "mytest@newtest.com",
            "phone_number": "09188765432",
            "username": "mytestnew",
            "password": "00009999",
            "full_name": "test mytest",
            "address": "local",
            "birth_date": "1997-04-11",
            "user_type": "1",
        }

        return super().setUp()

    def test_register_valid(self):
        response = self.client.post(self.register_url, self.register_data)
        self.assertEquals(response.status_code, 201)


class Login(SetupTest):
    def setUp(self):
        self.data = {
            "username": "test",
            "password": "123456"
        }
        self.profile_not_exist_data = {
            "username": "not found username",
            "password": "not found password"
        }
        return super().setUp()

    def test_login_(self):
        response = self.client.post(self.login_url, self.data)
        self.assertEquals(response.status_code, 200)

    def test_profile_not_exist(self):
        response = self.client.post(self.login_url, self.profile_not_exist_data)
        self.assertEquals(response.status_code, 400)


class ForgetPassword(SetupTest):
    def setUp(self):
        self.data = {
            "mobile": "12345678910"
        }
        return super().setUp()

    def test_forget_password(self):
        response = self.client.post(self.forget_password_url, self.data)
        self.assertEquals(response.status_code, 200)


class ConfirmPassword(SetupTest):
    def setUp(self):
        self.equal_data = {
            "code": "1234",
            "password": "654321",
            "confirm_password": "6543d21"
        }
        self.unequal_data = {
            "code": "1234",
            "password": "123456",
            "confirm_password": "654321"
        }
        self.incomplete_data = {
            "password": "123456",
            "confirm_password": "654321"
        }
        return super().setUp()

    def test_confirm_equal_password(self):
        response = self.client.post(self.confirm_password_url, self.equal_data)
        self.assertEquals(response.status_code, 200)

    def test_confirm_unequal_password(self):
        response = self.client.post(self.confirm_password_url, self.unequal_data)
        self.assertEquals(response.status_code, 400)

    def test_not_send_otp_code(self):
        response = self.client.post(self.confirm_password_url, self.incomplete_data)
        self.assertEquals(response.status_code, 400)
