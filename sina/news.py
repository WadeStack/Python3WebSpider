import requests
from lxml import etree
import csv

url = 'https://news.sina.com.cn/'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
s = etree.HTML(html)
file = s.xpath('//*[@id="blk_gjxw_011"]/li/a')


with open('data.csv','w',encoding='utf-8')as csvfile:
    writer = csv.writer(csvfile)
    for i in file:
        title = i.xpath('./text()')[0]
        url = i.xpath('./@href')[0]
        writer.writerow([title,url])



