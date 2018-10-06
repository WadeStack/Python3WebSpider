import requests
from lxml import etree
import time

#打印信息
def type_information(url):
    html = requests.get(url).text
    s = etree.HTML(html)
    file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
    for div in file:
        title = div.xpath('./tr/td[2]/div[1]/a/@title')[0]      # 书名
        score = div.xpath("./tr/td[2]/div[2]/span[2]/text()")[0]    # 评分
        num = div.xpath("./tr/td[2]/div[2]/span[3]/text()")[0].strip("(").strip().strip(")")    # 评价人数
        scrible = div.xpath("./tr/td[2]/p[2]/span/text()")       #   一句话描述
        time.sleep(1)
        if len(scrible) > 0:
            if len(num) > 0:
                print("{} {} {} {}".format(title, score, num, scrible[0]))
            else:
                print("{} {} {}".format(title, score, scrible))
        else:
            if len(num) > 0:
                print("{} {} {}".format(title, score, num))
            else:
                print("{} {}".format(title, score))

def main ():
    for a in range(10):
        url = 'https://book.douban.com/top250?start={}'.format(a*25)
        type_information(url)

main()
