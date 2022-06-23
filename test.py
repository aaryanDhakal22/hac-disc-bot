import unittest
from tz_manager import *
from datetime import datetime


class TestTimeZone(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self) -> None:
        pass

    def test_is_a_time_zone(self):
        self.assertTrue(is_timezone("Asia/Kathmandu"))
        self.assertFalse(is_timezone("123"))

    def test_correct_time(self):
        self.assertEqual(
            time_for_zone(
                [
                    "Asia/Kathmandu",
                ]
            ),
            {
                "Asia/Kathmandu": datetime.now().strftime("%I:%M %p"),
            },
        )

    def test_multiple_timezone(self):
        self.assertEqual(
            time_for_zone(["Asia/Kathmandu", "UTC"]),
            {
                "Asia/Kathmandu": datetime.now().strftime("%I:%M %p"),
                "UTC": datetime.utcnow().strftime("%I:%M %p"),
            },
        )

    def test_stored_timezone(self):
        self.assertEqual(
            return_tzs_for_stored(),
            {
                "Asia/Kathmandu": datetime.now().strftime("%I:%M %p"),
                "UTC": datetime.utcnow().strftime("%I:%M %p"),
            },
        )
