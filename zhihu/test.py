import requests
import json
import time
from lxml import etree
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
}
#
# def get_info(url_token):
#     url = 'https://www.zhihu.com/people/'+str(url_token)
#     html = requests.get(url,headers=headers).text
#     soup = BeautifulSoup(html,'lxml')
#     # print(soup)
#     name = soup.find_all('span', {'class': 'name'})
#     print(name)
#
#
#
#
# url_token = 'tnt-freedom'
# get_info(url_token)

# 获取所有id

# 获取问题的id
def get_id(offset):
    id = []
    for i in range(offset):
        i = i * 5
        url = 'https://www.zhihu.com/api/v4/search_v3?t=general&q=%E7%94%B7%E6%80%A7%E5%A5%B3%E6%80%A7%E5%8C%96&correction=1&offset=' + str(
            i)
        html = requests.get(url, headers=headers).json().get('data')
        for i in html:
            if 'object' in i:
                i = i['object']
                if 'question' in i:
                    id.append(i['question']['id'])
                    print(i['question']['id'])
    return id

# 获取问题的URL和回答数
def get_pn(id):
    for i in id:
        url = 'https://www.zhihu.com/question/'+str(i)
        html = requests.get(url, headers=headers).text
        s = etree.HTML(html)
        pn = s.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div[1]/h4/span/text()')[0] #获得每个问题的回复数
        print(pn)


# 获取个人信息
def get_info(url_token):
    url = 'https://www.zhihu.com/people/'+str(url_token)+'/activities'
    html = requests.get(url, headers=headers).text
    s = etree.HTML(html)
    headline = s.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[2]/text()')[0]
    # place = s.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/text()')
    work = s.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/text()')[0]
    # intro = s.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/div/div/div')
    print("{} {}".format(headline,work))




def main():
    url_token = 'tao-hua-kai-77'
    get_info(url_token)


main()