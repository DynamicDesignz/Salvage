import scrapy

class OtomotoSpider(scrapy.Spider):
    name = "otomoto"

    def start_requests(self):
        urls = []
        with open("__urls", 'r') as config_file:
            for line in config_file:
                if line.startswith("http"):
                    urls.append(line)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for offer in response.css('div.offer-item__content'):
            yield {
                    'Price': offer.css('span.offer-price__number::text').extract_first().replace(" ", ""),
                    'Year': offer.css('[data-code=year]>span::text').extract_first(),
                    'Mileage': offer.css('[data-code=mileage]>span::text').extract_first().replace(" ", ""),
                    'Fuel type': offer.css('[data-code=fuel_type]>span::text').extract_first(),
                    'Link': offer.css('a.offer-title__link::attr(href)').extract_first(),
                    }
        next_page = response.css('li.next>a::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

