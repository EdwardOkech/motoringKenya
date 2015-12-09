import scrapy
from motoringKenya.items import ChekiItem

class ChekiSpider(scrapy.Spider):
    """
    Spider that crawls checki .
    """
    name = "cheki"
    allowed_domains = ["cheki.co.ke"]
    start_urls = [
        "https://www.cheki.co.ke/search/saloons"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response,body)
            for sel in response.xpath('//ul/li'):
                item = ChekiItem()
                item['title'] = sel.xpath('a/text()').extract()
                item['desc'] = sel.xpath('text()').extract()
                yield item
