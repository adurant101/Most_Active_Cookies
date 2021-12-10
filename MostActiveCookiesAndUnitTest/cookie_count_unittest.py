import unittest
from most_active_cookie import Cookies

class TestCookieCount(unittest.TestCase):
    cookie = Cookies("cookie_log.csv", "2018-12-08")
    file_info = cookie.read_file()
    cookie_actual = cookie.get_cookie_and_time()
    cookie_count_actual = cookie.cookies_count()
    highest_count_cookies_actual = cookie.get_cookies_with_highest_count()
    # Correct values for testing
    file_expected = [{'cookie': 'AtY0laUfhglK3lC7',
    'timestamp': '2018-12-09T14:19:00+00:00'},
    {'cookie': 'SAZuXPGUrfbcn5UA', 'timestamp': '2018-12-09T10:13:00+00:00'},
    {'cookie': '5UAVanZf6UtGyKVS', 'timestamp': '2018-12-09T07:25:00+00:00'},
    {'cookie': 'AtY0laUfhglK3lC7', 'timestamp': '2018-12-09T06:19:00+00:00'},
    {'cookie': 'SAZuXPGUrfbcn5UA', 'timestamp': '2018-12-08T22:03:00+00:00'},
    {'cookie': '4sMM2LxV07bPJzwf', 'timestamp': '2018-12-08T21:30:00+00:00'},
    {'cookie': 'fbcn5UAVanZf6UtG', 'timestamp': '2018-12-08T09:30:00+00:00'},
    {'cookie': '4sMM2LxV07bPJzwf', 'timestamp': '2018-12-07T23:30:00+00:00'}]

    cookie_time = [['AtY0laUfhglK3lC7', '2018-12-09T14:19:00+00:00'],
    ['SAZuXPGUrfbcn5UA', '2018-12-09T10:13:00+00:00'],
    ['5UAVanZf6UtGyKVS', '2018-12-09T07:25:00+00:00'],
    ['AtY0laUfhglK3lC7', '2018-12-09T06:19:00+00:00'],
    ['SAZuXPGUrfbcn5UA', '2018-12-08T22:03:00+00:00'],
    ['4sMM2LxV07bPJzwf', '2018-12-08T21:30:00+00:00'],
    ['fbcn5UAVanZf6UtG', '2018-12-08T09:30:00+00:00'],
    ['4sMM2LxV07bPJzwf', '2018-12-07T23:30:00+00:00']]

    count_dict = {'SAZuXPGUrfbcn5UA': 1, '4sMM2LxV07bPJzwf': 1,
    'fbcn5UAVanZf6UtG': 1}
    cookies_with_highest_count = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf',
    'fbcn5UAVanZf6UtG']

    def test_read_file(self):
        # Test output for read file is correct
        self.assertEqual(self.__class__.file_expected,self.__class__.file_info,
        "Read file failed")

    def test_get_cookie_and_time(self):
        # Test output for cookie and time
        self.assertEqual(self.__class__.cookie_time, self.__class__.cookie_actual,
        "Get cookie and time failed")

    def test_cookie_count(self):
        # Test output for cookie count
        self.assertEqual(self.__class__.count_dict, self.__class__.cookie_count_actual,
        "Get cookie count failed")

    def test_cookies_highest_count(self):
        # Test output for cookies with highest count
        self.assertEqual(self.__class__.cookies_with_highest_count,
        self.__class__.highest_count_cookies_actual, "Highest count cookies failed")
