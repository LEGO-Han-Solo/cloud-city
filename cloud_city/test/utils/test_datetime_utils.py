from cloud_city.utils import get_str_timestamp, TIMESTAMP_FMT
from datetime import datetime


def test_get_timestamp():
    timestamp = get_str_timestamp()
    assert type(timestamp) == str
    assert datetime.strptime(timestamp, TIMESTAMP_FMT)
