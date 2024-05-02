import unittest
from main import app, get_lat_or_long_bad_request_string


class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_lat_or_long_bad_request_string(self):
        test_table = {
            ("invalid", 0): False,  # test invalid latitude
            (0, "invalid"): False,  # test invalid longitude
            (0, 0): True,  # test in range
            (-200, 0): False,  # test out of range latitude
            (0, -200): False,  # test out of range longitude
        }
        for (lat, long), error_msg_is_none in test_table.items():
            actual_error_msg = get_lat_or_long_bad_request_string(lat, long)
            if error_msg_is_none:
                self.assertIsNone(actual_error_msg)
            else:
                self.assertIsNotNone(actual_error_msg)

    def test_invalid_parameters_route(self):
        response = self.app.get('/weather?lat=100&long=200')
        self.assertEqual(response.status_code, 400)

    def test_success(self):
        response = self.app.get('/weather?lat=37.7749&long=-122.4194')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
