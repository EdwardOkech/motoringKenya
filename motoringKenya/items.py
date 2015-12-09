
import scrapy


class ChekiItem(scrapy.Item):
    """
    Define item models for checki.co.ke website
    """
    title = scrapy.Field()
    desc = scrapy.Field()

