from datetime import datetime
from pytz import country_timezones, timezone
from pytz.exceptions import UnknownTimeZoneError
import pycountry
from Assignment_2.logger import logger, log_exception


class Country(object):
    """
    This class defines Country
    and methods for getting country code, time zone, and current time in country
    """
    def __init__(self, country):
        self.country = country
        print(self.country)

    def get_country_code(self):
        """
        Returns the country code
        :param self: Instance of Country
        :return: Country code
        :rtype: str
        """
        try:
            return pycountry.countries.get(name=self.country).alpha_2
        except (KeyError, AttributeError) as e:
            logger.error(e)
            logger.error(log_exception())

    def get_time_zone(self):
        """
        Returns the timezone of the country
        :param self: Instance of Country
        :return: timezone
        :rtype: str
        """
        try:
            timezone_country = {}
            country_code = self.get_country_code()
            for countrycode in country_timezones:
                timezones = country_timezones[countrycode]
                for tz in timezones:
                    timezone_country[countrycode] = tz
            print(country_code)
            return timezone_country[country_code]
        except (KeyError, ValueError, AttributeError, TypeError) as e:
            logger.error(e)
            logger.error(log_exception())

    def get_current_time(self):
        """
        Returns the current time in specific country
        :param self: Instance of Country
        :return: current_time
        :rtype: datetime.datetime
        """
        try:
            tz = self.get_time_zone()
            now = datetime.now(timezone(tz))
        except (AttributeError, UnknownTimeZoneError) as e:
            logger.error(e)
            logger.error(log_exception())
        return now


class CountryDelay(Country):
    """
    Manages delay on the basic od schedule time and selected country
    """
    def __init__(self, country, schedule_time):
        try:
            super().__init__(country)
            self.schedule_time = schedule_time
        except (AttributeError, TypeError) as e:
            logger.error(e)
            logger.error(log_exception())

    def get_delay(self):
        """
        Returns the time in delivery of message, based on country and schedule time
        :param self: Instance of CountryDelay
        :return: time remaining in sending message (seconds)
        :rtype: int
        """
        try:
            time_now = self.get_current_time().timestamp()
            schedule_time = datetime.strptime(self.schedule_time, "%Y-%m-%d %I:%M %p").timestamp()
            return int(schedule_time-time_now)
        except ValueError as e:
            logger.error(e)
            logger.error(log_exception())
