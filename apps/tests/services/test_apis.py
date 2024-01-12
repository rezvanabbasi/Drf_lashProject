from .test_setup import SetupTest


class LashService(SetupTest):
    def setUp(self):
        self.lash_service_data = {
            "title": "test",
            "material": "test material"
        }
        self.reserve_lash_service_date = {
            "comment": "test comment2"
        }
        return super().setUp()

    def test_create_lash_service(self):
        response = self.client.post(self.lash_service_url, self.lash_service_data)
        self.assertEquals(response.status_code, 201)

    def test_reserve_service(self):
        response = self.client.post(self.reserve_service_url, self.reserve_lash_service_date)
        self.assertEquals(response.status_code, 201)
