import scrapy
from scrapy.crawler import CrawlerProcess

from .. import db
from ..models import News
from .scrape import scrape_article
from .summarizer import summarize


class EkantipurSpider(scrapy.Spider):
    name = 'enews'
    category = ['sports', 'business', 'lifestyle']

    start_urls = [
        'https://thehimalayantimes.com/category/nepal'
    ]

    def parse(self, response):
        for i in range(3):
            headline = response.css('.col-sm-4 a').css('::text').extract()[i]
            link = response.css('h4 a::attr(href)').extract()[i]
            category = link.split('/')[3]
            summary = summarize(scrape_article(link))
            news = News(headline=headline, url=link, summarized_body=summary, category=category)
            db.session.add(news)
        db.session.commit()

        for objects in EkantipurSpider.category:
            next_page = f'https://thehimalayantimes.com/category/{objects}/'
            yield response.follow(next_page, callback=self.parse)

def run_spider():
    process = CrawlerProcess()
    process.crawl(EkantipurSpider)
    process.start()
