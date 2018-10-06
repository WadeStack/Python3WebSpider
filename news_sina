import requests
from lxml import etree

url = 'https://news.sina.com.cn/'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
s = etree.HTML(html)
file = s.xpath('//*[@id="blk_gjxw_011"]/li/a')
for i in file:
    title = i.xpath("./text()")[0]
    url = i.xpath('./@href')[0]
    print("{}      {}".format(title,url))
