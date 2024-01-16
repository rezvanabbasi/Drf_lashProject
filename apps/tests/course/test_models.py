from .test_setup import SetupTest


class CourseTest(SetupTest):
    def test_course_type(self):
        self.assertEquals(str(self.course_type), self.course_type.title)

    def test_course(self):
        self.assertEquals(str(self.course), self.course.title)

    def test_course_reservation(self):
        self.assertEquals(str(self.course_reservation), self.course_reservation.reserve_date)
