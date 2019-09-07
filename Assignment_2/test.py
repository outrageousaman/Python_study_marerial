from datetime import datetime, timedelta
from pytz import timezone
import unittest

from Assignment_2.country import Country, CountryDelay
from Assignment_2.message import MessageScheduler
from Assignment_2.service import run_message_scheduler

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country_1 = Country('India')
        self.country_2 = Country('USA')

    def test_country_name(self):
        self.assertEqual(self.country_1.country, 'India')
        self.assertEqual(self.country_2.country, 'USA')


class TestCountryDelay(unittest.TestCase):
    def setUp(self):
        schedule_time = datetime.now(timezone('Asia/Kolkata')) + timedelta(minutes=100)
        schedule_time_str = schedule_time.strftime('%Y-%m-%d %I:%m %p')
        self.country = CountryDelay('India', schedule_time_str)

    def test_country_code(self):
        self.assertEqual(self.country.get_country_code(), 'IN')

    def test_country_timezone(self):
        self.assertEqual(self.country.get_time_zone(), 'Asia/Kolkata')

    def test_country_delay(self):
        self.assertLessEqual(self.country.get_delay(), 6000)

    def test_get_current_time(self):
        self.assertAlmostEqual(int(self.country.get_current_time().timestamp()), int(datetime.now().timestamp()))


class TestMessageScheduler(unittest.TestCase):
    def setUp(self):
        schedule_time = datetime.now(timezone('Asia/Kolkata')) + timedelta(minutes=100)
        self.schedule_time_str = schedule_time.strftime('%Y-%m-%d %I:%m %p')
        self.number = '9999999999'
        self.body = 'test_message'
        self.country = 'India'
        self.message_scheduler = MessageScheduler(self.number, self.body, self.country, self.schedule_time_str)

    def test_message(self):
        self.assertEqual(self.message_scheduler.to, self.number)
        self.assertEqual(self.message_scheduler.body, self.body)

    def test_message_country_delay(self):
        self.assertEqual(self.message_scheduler.country_delay.country, self.country)
        self.assertLessEqual(self.message_scheduler.country_delay.get_delay(), 6000)
        self.assertEqual(self.message_scheduler.country_delay.get_country_code(), 'IN')

    def test_message_queue(self):
        self.assertIsInstance(self.message_scheduler.list_queued_message(), list)


class TestMessageScheduler(unittest.TestCase):
    def setUp(self):
        self.body = 'test_message'
        self.file_name = 'customers.csv'
        self.country = 'India'
        now = datetime.now(timezone('Asia/Kolkata')) + timedelta(seconds=10)
        self.schedule_time_str = now.strftime('%Y-%m-%d %I:%m %p')
        self.scheduler_status = run_message_scheduler(self.file_name, self.schedule_time_str, self.body)

    def test_scheduler(self):
        self.assertEqual(self.scheduler_status['status'].lower(), 'success')


if __name__ == '__main__':
    unittest.main()