import scrapy

class MySpider(scrapy.Spider):
    name = 'spider_adi'

    custom_settings = {
      'ROBOTSTXT_OBEY': False
    }

    def start_requests(self):
        url = 'http://webcache.googleusercontent.com/search?q=cache:https://www.evrensel.net/haber/117890/hasar-tespitlerinde-rapor-celiskisi'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        title = response.xpath('//*[@id="metin"]/h1').get()
        print("Başlık:", title)