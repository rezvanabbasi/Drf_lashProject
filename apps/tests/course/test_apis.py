from django.urls import reverse

from .test_setup import SetupTest


class CourseTest(SetupTest):
    def test_course(self):
        url = reverse("course")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
