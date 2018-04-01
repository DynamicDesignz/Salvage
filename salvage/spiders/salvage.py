import scrapy
import re

class Salvage(scrapy.Spider):
    name = "salvage"
    
    def start_requests(self):
        urls = []
        with open("__urls", 'r') as urls_file:
            for line in urls_file:
                if line.startswith("http"):
                    urls.append(line)

        with open("config", 'r') as config_file:
            for line in config_file:
                if line.startswith("PRICE_MIN"):
                    global PRICE_MIN
                    PRICE_MIN = re.findall(r'\d+', line)[0]
                elif line.startswith("PRICE_MAX"):
                    global PRICE_MAX
                    PRICE_MAX = re.findall(r'\d+', line)[0]
                elif line.startswith("FUEL"):
                    global FUEL
                    FUEL = re.findall(r'[:\s](\w*)', line)[0]
                elif line.startswith("BODY"):
                    global BODY
                    BODY = re.findall(r'[:\s](\w*)', line)[0]
                elif line.startswith("YEAR"):
                    global YEAR
                    YEAR = re.findall(r'\d+', line)[0]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(PRICE_MIN[0])
        print(PRICE_MAX[0])
        print(FUEL[0])
        for offer in response.css('div.offer-item__content'):
            price = offer.css('span.offer-price__number::text').extract_first().replace(" ", "")
            fuel = offer.css('[data-code=fuel_type]>span::text').extract_first()
            year = offer.css('[data-code=year]>span::text').extract_first()
            mileage = offer.css('[data-code=mileage]>span::text').extract_first().replace(" ", "")
            link = offer.css('a.offer-title__link::attr(href)').extract_first()
            
            if int(price) >= int(PRICE_MIN) and int(price) <= int(PRICE_MAX) and str(fuel) == str(FUEL) and int(year) >= int(YEAR):
               yield {
                    'Price': price,
                    'Year': year,
                    'Mileage': mileage,
                    'Fuel type': fuel,
                    'Year': year,
                    'Link': link,
                    } 

        next_page = response.css('li.next>a::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)
