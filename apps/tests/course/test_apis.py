from .test_setup import SetupTest


class CourseTypeTest(SetupTest):
    def setUp(self):
        self.course_type_data = {
            "title": "test title"
        }
        return super().setUp()

    def test_course_type_create(self):
        response = self.client.post(self.course_type_url, self.course_type_data)
        self.assertEquals(response.status_code, 201)


class CourseTest(SetupTest):
    def setUp(self):
        self.course_data = {
            "title": "test"
        }
        self.reserve_course_data = {
            "student_id": 1,
            "teacher_id": 1
        }
        return super().setUp()

    def test_create_course(self):
        response = self.client.post(self.course_url, self.course_data)
        self.assertEquals(response.status_code, 201)

    def test_get_course(self):
        response = self.client.get(self.course_url)
        self.assertEquals(response.status_code, 200)

    def test_reserve_course(self):
        response = self.client.post(self.course_reservation_url, self.reserve_course_data)
        self.assertEquals(response.status_code, 200)

    def test_get_course_reserve(self):
        response = self.client.get(self.course_reservation_url)
        self.assertEquals(response.status_code, 200)
