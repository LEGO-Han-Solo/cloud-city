from cloud_city.scrappers import LegenioCzScrapper
from cloud_city.constants import PEREX_FIELD_NAME, PRICE_FIELD_NAME, IN_STOCK_FIELD_NAME, TIMESTAMP_FIELD_NAME, \
    NAME_FIELD_NAME


def test_legenio_cz_scrapper():
    scrapper = LegenioCzScrapper(timeout=0)
    limit = 2
    legos = scrapper.scrap_legos(limit=limit)
    assert len(legos) == limit
    for item in legos:
        assert type(item) == dict
        assert type(item[NAME_FIELD_NAME]) == str
        assert type(item[PEREX_FIELD_NAME]) == str
        assert type(item[PRICE_FIELD_NAME]) == float
        assert type(item[IN_STOCK_FIELD_NAME]) == bool
        assert type(item[TIMESTAMP_FIELD_NAME]) == str
