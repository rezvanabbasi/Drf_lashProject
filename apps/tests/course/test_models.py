from apps.course.models import Course

from .test_setup import SetupTest


#
class ModelTest(SetupTest):
    def test_course_model(self):
        course = Course.objects.first()
        self.assertEquals(str(course), course.title)

    
