from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory


class SetupTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        return super().setUpTestData()

    def setUp(self):
        self.factory = APIRequestFactory()
        self.home_url = reverse('home')

        return super().setUp()

    def tearDown(self):
        super().tearDown()

    @classmethod
    def tearDownClass(cls):
        print("finished tests of users app")
        return super().tearDownClass()

