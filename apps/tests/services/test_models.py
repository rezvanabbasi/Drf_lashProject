from .test_setup import SetupTest


class ServiceModelTest(SetupTest):

    def test_service(self):
        self.assertEquals(str(self.service), self.service.title)

    def test_reserve_service(self):
        self.assertEquals(str(self.reserve_service), self.reserve_service)
