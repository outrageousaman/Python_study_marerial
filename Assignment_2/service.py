import csv
import traceback

from Assignment_2.message import MessageScheduler, s
from Assignment_2.logger import logger, log_exception


def run_message_scheduler():
    """
    :return:
    """
    logger.info('starting process')
    file_name = input('Enter the name of .csv File : ')
    schedule_time = input('Enter the schedule time in format "yyyy-mm-dd hh:mm AM/PM" : ')
    body = input('body of the message : ')
    logger.info(f'file name: {file_name} , tentative run time: {schedule_time}, message body: {body}')

    logger.info(f'reading contacts from file {file_name}')
    try:
        with open(file_name, 'r') as f:
            data = csv.reader(f)
            for row in data:
                phone_number, country = row
                logger.info('record =  phone number : ' + phone_number + ' country :' + country)
                m = MessageScheduler(phone_number.strip(), body.strip(), country.strip(), schedule_time)
                logger.info(f'Message for {phone_number} added in queue')
                m.send_message()
    except (FileNotFoundError, IOError, ValueError) as e:
        logger.error(e)
        logger.error(log_exception())
    queued_messages = MessageScheduler.list_queued_message()
    logger.info('queued messages')
    logger.info(queued_messages)
    s.run()
    logger.info('Completed Successfully')
    return queued_messages


if __name__ == '__main__':
    run_message_scheduler()