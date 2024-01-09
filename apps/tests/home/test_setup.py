from model_bakery import baker
from rest_framework.test import APITestCase

from apps.course.models import Course


class SetupTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Course)
        return super().setUpTestData

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        print("finished tests of home app")
        return super().tearDownClass()
