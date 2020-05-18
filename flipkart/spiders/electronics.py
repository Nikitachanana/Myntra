# -*- coding: utf-8 -*-
import scrapy
from ..items import FlipkartItem
import csv


class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    page = 2
    start_urls = ['https://www.flipkart.com/mobiles-accessories/pr?sid=tyy&marketplace=FLIPKART&page=1']

    def parse(self, response):
        category = response.css('._2yAnYN::text')
        data = response.css('div._3O0U0u')
        for d in data:
            object= d.css('div._3liAhj')
            for i in object:
                name = i.css('._2cLu-l::text').extract_first()
                price = i.css('._1vC4OE::text').extract_first()
                rating = i.css('.hGSR34::text').extract_first()

                yield {

                    'name': name,
                    'price': price,
                    'rating': rating
                }
        next_page= 'https://www.flipkart.com/mobiles-accessories/pr?sid=tyy&marketplace=FLIPKART&page='+str(ElectronicsSpider.page)
        if ElectronicsSpider.page <=11:
            ElectronicsSpider.page +=1
            yield response.follow(next_page, callback=self.parse)











