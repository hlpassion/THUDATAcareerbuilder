# -*- coding: utf-8 -*-

from scrapy import cmdline
import time

cmdline.execute("scrapy crawl careerbuilder -s CLOSESPIDER_ITEMCOUNT=500".split())