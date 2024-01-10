from unittest import TestCase

from apps.services.models import LashService


class ServiceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        LashService.objects.create(title='اکستنشن مژه')
