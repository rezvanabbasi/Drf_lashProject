from apps.course.models import Course

from django.test import TestCase


class CourseTest(TestCase):

    def setUp(self):
        Course.objects.create(
            title="اکستنشن مژه تست",
            teacher_id='1',
            course_capacity=4,
            course_sessions=5,
        )

    def teacher_id_test(self):
        course = Course.objects.get(title='اکستنشن مژه تست')
        self.assertEquals(course.teacher_id, 1)
