# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from ..items import ThudatacareerbuilderItem


class CareerbuilderSpider(scrapy.Spider):
    name = 'careetbuilder'
    allow_domains = ["careerbuilder.com"]

    start_urls = ["http://www.careerbuilder.com/job/J3H4VH6WVCJP37V26WC?"
                  "ipath=JRG1&searchid=2ea1e6c9-541d-46ad-995a-5fb1c842cd29&siteid=cbnsv"]


    def parse_job_info(self, response):
        sel = Selector(response)
        item = ThudatacareerbuilderItem()
        print("parse job info from %s" % response.url)

        item['position_name'] = ''.join(sel.xpath('//div[@class="small-12 item"]/h1').extract())
        item['position_category'] = None
        