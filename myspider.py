import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["uzmanpara.milliyet.com.tr"]
    start_urls = ["https://uzmanpara.milliyet.com.tr/canli-borsa/"]

    def parse(self, response):
        table_rows = response.css('tr.zebra')  # Tüm zebra sınıfına sahip tr etiketlerini seçer

        for row in table_rows:
            currency = row.css('td.currency b::text').get()  # Hisse senedi adını çeker
            price = row.css('td.center#h_td_fiyat_id_{}::text'.format(currency)).get()  # Fiyatı çeker
            percentage = row.css('td.center#h_td_yuzde_id_{}::text'.format(currency)).get()  # Yüzdeyi çeker
            time = row.css('td.center#h_td_zaman_id_{}::text'.format(currency)).get()  # Zamanı çeker

            print("Currency:", currency)
            print("Price:", price)
            print("Percentage:", percentage)
            print("Time:", time)