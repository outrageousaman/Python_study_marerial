import sched
import time
from Assignment_2.country import CountryDelay
from Assignment_2.logger import logger, log_exception

s = sched.scheduler(time.time, time.sleep)


class Message(object):
    """
    Message class
    """
    def __init__(self, to, body):
        """
        Initialize Message
        :param to: Receiver phone number
        :param body: Body text
        """
        self.to = to
        self.body = body


class MessageScheduler(Message):
    """
    MessageScheduler class
    """
    def __init__(self, to, body, country, schedule_time):
        """
        Initialize MessageScheduler
        :param to: Receiver phone number
        :param body: Body text
        :param country: Country name
        :param schedule_time: Schedule Time
        """
        try:
            super().__init__(to, body)
            self.country_delay = CountryDelay(country, schedule_time)
        except (AttributeError, TypeError) as e:
            logger.error(e)
            logger.error(log_exception())

    def message_sender(self):
        """
        Send the message
        :return: response from sender API
        """
        print('to : ', self.to)
        print('body : ', self.body)

    def send_message(self):
        """
        schedules the message
        :return: None
        """
        try:
            delay = self.country_delay.get_delay()
            s.enter(delay, 1, self.message_sender)
        except (AttributeError, ValueError) as e:
            logger.error(e)
            logger.error(log_exception())


    @staticmethod
    def list_queued_message():
        """
        :return: list of queued messages
        """
        return s.queue
