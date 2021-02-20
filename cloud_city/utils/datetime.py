import pytz
from datetime import datetime

TIMEZONE = pytz.timezone("Europe/Prague")
TIMESTAMP_FMT = '%Y-%m-%d %H:%M:%S'


def get_str_timestamp():
    timestamp = datetime.now(tz=TIMEZONE)
    return timestamp.strftime(TIMESTAMP_FMT)
