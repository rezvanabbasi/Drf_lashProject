from .test_setup import SetupTest


class UserTypeTest(SetupTest):
    def setUp(self):
        self.type_data = {
            "title": "مربی",
            "description": "this is test"
        }
        return super(UserTypeTest, self).setUp()

    def test_user_type_create(self):
        response = self.client.post(self.type_url, self.type_data)
        self.assertEquals(response.status_code, 201)


class RegisterTest(SetupTest):
    def setUp(self):
        self.register_data = {
            "id":2,
            "email": "mytest@newtest.com",
            "phone_number": "09188765432",
            "username": "mytestnew",
            "password": "00009999",
            "full_name": "test mytest",
            "address": "local",
            "birth_date": "1997-04-11",
            "user_type": "1",
        }
        return super(RegisterTest, self).setUp()

    def test_register_valid(self):
        response = self.client.post(self.register_url, self.register_data)
        self.assertEquals(response.status_code, 201)
