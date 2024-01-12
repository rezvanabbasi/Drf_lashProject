from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from apps.course.models import Course, CourseType, CourseReservation


class SetupTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        return super().setUpTestData

    def setUp(self):
        self.factory = APIRequestFactory()
        self.course_type_url = reverse('course-type')
        self.course_url = reverse('course')
        self.course_reservation_url = reverse('course-reservation')

        # create course
        self.course = Course.objects.create(title="course test")

        # create course type
        self.course_type = CourseType.objects.create(title="type test")

        # create course reservation
        self.course_reservation = CourseReservation.objects.create()

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        print("finished tests of course app")
        return super().tearDownClass()
