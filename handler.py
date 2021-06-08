import logging
from venmo_client import VenmoClient
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    client = VenmoClient("username", "password")
    print(client.get_user("Richard-Deng-2"))

    logger.info("Full event: %s", event)
