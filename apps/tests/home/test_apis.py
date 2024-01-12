from .test_setup import SetupTest


class HomeTest(SetupTest):

    def test_home(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
