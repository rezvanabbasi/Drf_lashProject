from .test_setup import SetupTest


class ServiceModelTest(SetupTest):

    def test_service(self):
        self.assertEquals(str(self.lash_service), self.lash_service.title)

    def test_reserve_service(self):
        self.assertEquals(str(self.reserve_service), self.reserve_service)
