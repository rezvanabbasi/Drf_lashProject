from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from apps.services.models import LashService, ReserveService


class SetupTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        return super().setUpTestData

    def setUp(self):
        self.factory = APIRequestFactory()
        # views
        self.lash_service_url = reverse('service')
        self.delete_update_service_url = reverse('delete-update-service')
        self.reserve_service_url = reverse('reserve-service')

        # create service
        self.lash_service = LashService.objects.create(
            title="test",
            material="test material"
        )

        # Reserve Service
        self.reserve_service = ReserveService.objects.create(comment="test comment")

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        print("finished tests of service app")
        return super().tearDownClass()
