from django.urls import reverse
from .test_setup import SetupTest


class HomeTest(SetupTest):

    def home_test(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
