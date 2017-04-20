# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from THUDATAcareerbuilder.items import ThudatacareerbuilderItem


class CareerbuilderSpider(scrapy.Spider):
    name = 'careerbuilder'
    allow_domains = ["careerbuilder.com"]
    search_fields = ['data analysis', 'big data', 'web crawler', 'visualization', 'Hadoop', 'Spark', 'Hive', 'HBase', 'SQL']
    
    urls = []
    for job in search_fields:
        url = 'http://www.careerbuilder.com/jobs-' + str(job).replace(' ', '-') + '?sort=date_desc'
        urls.append(url)    
    start_urls = urls
    
    def start_requests(self):
        for job_url in self.start_urls:
            yield scrapy.Request(url=job_url, callback=self.parse_career_list)
    
    
    def parse_career_list(self, response):
        sel = Selector(response)
        url_prefix = 'http://www.careerbuilder.com'
        job_urls = sel.xpath('//div[@class="column small-10"]/h2/a/@href').extract()
        for job_url in job_urls:
            url = url_prefix + job_url
            yield scrapy.Request(url=url, callback=self.parse_job_info)
            
        # 判断下一页
        next_page_url = ''.join(sel.xpath('//a[@aria-label="Next Page"]/@href').extract())
        next_page_label = ''.join(sel.xpath('//a[@aria-label="Next Page"]/@aria-disabled').extract())
        if next_page_label == 'false':
            yield scrapy.Request(url=next_page_url, callback=self.parse_career_list)
        
    
    
    
    def parse_job_info(self, response):
        sel = Selector(response)
        item = ThudatacareerbuilderItem()
        print("parse job info from %s" % response.url)

        item['position_name'] = ''.join(sel.xpath('//div[@class="small-12 item"]/h1/text()').extract()).strip()
        item['position_category'] = 'NULL'
        item['department'] = 'NULL'
        item['workplace'] = ''.join(sel.xpath('//div[@class="small-12 item"]/h2/text()').extract()).strip().split('\n')[-1]     # 工作地点
        
        # Job Snapshot
        job_facts_item = sel.xpath('//div[@class="tag"]/text()').extract()
        job_facts_item = [i.strip() for i in job_facts_item]
        item['employment_type'] = job_facts_item[0]
        
        # 获取工作经验和学历、薪资，从工作的各个标签中获取包含Experience，Degree，$来获取
        item['experience'] = 'NULL'
        item['education'] = 'NULL'
        item['salary'] = 'NULL'
        for i in job_facts_item:
            if 'Experience' in i: 
                item['experience'] = i.split("-")[-1]
            elif 'Degree' in i:
                item['education'] = i.split("-")[-1]
            elif '$' in i:
                item['salary'] = i
            
        item['major'] = 'NULL'
        item['num_recruit'] = 'NULL'
        item['temptation'] = 'NULL'
        
        # 获取职位描述和职位需求
        description = sel.xpath('//div[@class="description"]')
        if len(description) == 1:
            item['description'] = ''.join(description.xpath('string(.)').extract()).strip()
            item['requirement'] = 'NULL'
        else:
            item['description'] = ''.join(description[0].xpath('string(.)').extract()).strip()
            item['requirement'] = ''.join(description[1].xpath('string(.)').extract()).strip()
        
        item['company_name'] =  ''.join(sel.xpath('//div[@class="small-12 item"]/h2/text()').extract()).strip().split('\n')[0]
        item['company_industry'] = ''.join(sel.xpath('//div[@class="job-facts item"]/div[@id="job-industry"]/text()').extract()).strip()                       # 公司行业
        item['company_nature'] = ''.join(sel.xpath('//div[@class="job-facts item"]/div[@id="job-categories"]/text()').extract()).strip()                       # 公司性质
        item['finance'] = 'NULL'
        item['company_size'] = 'NULL'
        item['company_homepage'] = 'NULL'
        item['post_date'] = ''.join(sel.xpath('//div[@class="small-12 item"]/h3/text()').extract()).strip()
        item['website'] = 'careerbuilder'
        item['url'] = response.url
        yield item
        
