import scrapy
from ..items import MinimalnewsItem


class EkantipurSpiderSpider(scrapy.Spider):
    name = 'enews'
    category = ['nepal', 'world', 'opinion', 'business', 'sports', 'lifestyle', 'entertainment', 'education',
                'science-technology']
    start_urls = [
        'https://thehimalayantimes.com/category/kathmandu/'
     ]

    def parse(self, response):
        items = MinimalnewsItem()

        for i in range(5):
            headline = response.css('.col-sm-4 a').css('::text').extract()[i]
            link = response.css('h4 a::attr(href)').extract()[i]

            items['headline'] = headline
            items['link'] = link

            yield items

        for objects in EkantipurSpiderSpider.category:
            next_page = 'https://thehimalayantimes.com/category/' + objects + '/'
            yield response.follow(next_page, callback=self.parse)





