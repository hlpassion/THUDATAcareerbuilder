# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import timedelta, date
import time
import csv
import xlwt
import re

file = xlwt.Workbook()
writeSheet = file.add_sheet("joblist", cell_overwrite_ok=True)
count = 0

class ThudatacareerbuilderPipeline(object):
    def process_item(self, item, spider):
        global count
        # ---------------发布时间-------------------
        # 格式有Posted 28 days ago | Posted 2 hours ago | Posted now | Posted 1 hour ago | Posted 1 day ago
        posted_date = item['post_date']
        if 'now' in posted_date or 'hour' in posted_date or 'hours' in posted_date:
            final_date = '{}/{}/{}'.format(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)
        elif 'day' in posted_date or 'days' in posted_date:
            num_day = ''.join(re.findall('\d+', posted_date))
            original_date = date.today() + timedelta(days = -1 * int(num_day))
            final_date = '{}/{}/{}'.format(original_date.year, original_date.month, original_date.day)
        item['post_date'] = final_date
        
        writeSheet.write(count, 0, item['position_name'])           # 职位名字
        writeSheet.write(count, 1, item['position_category'])       # 分类标签
        writeSheet.write(count, 2, item['department'])              # 部门
        writeSheet.write(count, 3, item['workplace'])               # 工作地点
        writeSheet.write(count, 4, item['employment_type'])         # 工作性质（全职实习）
        writeSheet.write(count, 5, item['experience'])              # 经验
        writeSheet.write(count, 6, item['education'])               # 学历
        writeSheet.write(count, 7, item['salary'])                  # 薪资
        writeSheet.write(count, 8, item['major'])                   # 专业
        writeSheet.write(count, 9, item['num_recruit'])             # 招聘人数
        writeSheet.write(count, 10, item['temptation'])             # 职位诱惑
        writeSheet.write(count, 11, item['description'])            # 岗位介绍
        writeSheet.write(count, 12, item['requirement'])            # 岗位要求
        writeSheet.write(count, 13, item['company_name'])           # 公司名称
        writeSheet.write(count, 14, item['company_industry'])       # 行业
        writeSheet.write(count, 15, item['company_nature'])         # 公司性质
        writeSheet.write(count, 16, item['finance'])                # 融资阶段
        writeSheet.write(count, 17, item['company_size'])           # 规模
        writeSheet.write(count, 18, item['company_homepage'])       # 主页
        writeSheet.write(count, 19, final_date)                     # 发布日期
        writeSheet.write(count, 20, item['website'])                # 发布网站
        writeSheet.write(count, 21, item['url'])                    # 原始URL
        file.save('THUDataPiCrawler_careerbuilder_2017_04_18.xls')
        count += 1
        print("write into excel successfully")        
