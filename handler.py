import calendar
import logging
import dateutil.parser
from venmo_client import VenmoClient
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    if 'time' in event:
        dt = dateutil.parser.parse(event['time'])
        client = VenmoClient("username", "password")
        print(client.get_user("Richard-Deng-2"))
        logger.info(
            "Thanks for calling me on %s at %s.",
            calendar.day_name[dt.weekday()], dt.time().isoformat())
    logger.info("Full event: %s", event)
