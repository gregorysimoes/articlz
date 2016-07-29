#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import html
import requests
import csv


# url to scrape
url = 'XXXXXX'

# add User-Agent
ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# GET requests to specified url
page = requests.get(url, headers=ua)
tree = html.fromstring(page.content)

# path to the element we are looking for
a = tree.xpath('//XXXXXXXX')

# write resultst in csvfile
with open('tests.csv', 'a+') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    writer.writerow(a)

# print results
# print a
