import unittest
import esp_server


class ServerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = esp_server.app.test_client()

    def test_index_load(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_testpage_load(self):
        response = self.app.get('/test/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
