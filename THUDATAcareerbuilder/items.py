# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThudatacareerbuilderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position_name = scrapy.Field()              # 职位名称
    position_category = scrapy.Field()          # 职位分类标签
    department = scrapy.Field()                 # 部门
    workplace = scrapy.Field()                  # 工作地点
    employment_type = scrapy.Field()            # 工作性质
    experience = scrapy.Field()                 # 工作经验
    education = scrapy.Field()                  # 学历
    salary = scrapy.Field()                     # 薪资
    major = scrapy.Field()                      # 专业要求
    num_recruit = scrapy.Field()                # 招聘人数
    temptation = scrapy.Field()                 # 职位诱惑
    description = scrapy.Field()                # 职位描述
    company_name = scrapy.Field()               # 公司名称
    company_industry = scrapy.Field()           # 公司行业
    company_nature = scrapy.Field()             # 公司性质
    finance = scrapy.Field()                    # 融资阶段
    company_size = scrapy.Field()               # 公司规模
    company_homepage = scrapy.Field()           # 公司主页
    post_date = scrapy.Field()                  # 发布日期
    website = scrapy.Field()                    # 发布网站
    url = scrapy.Field()                        # 原始URL