from apps.tests.users.test_setup import SetupTest


class ModelTest(SetupTest):

    def test_user_type(self):
        self.assertEquals(str(self.user_type), self.user_type.title)

    def test_profile_model(self):
        self.assertEquals(str(self.profile), self.profile.email)

    def test_otp_code(self):
        self.assertEquals(str(self.otp_code), self.otp_code.mobile)
#
