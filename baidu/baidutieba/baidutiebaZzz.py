import requests
from lxml import etree
import time


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
}

# 获得帖子的所有url
def get_urls(cnt):
    list_url = []
    for i in range(1,cnt+1):
        url_ = 'https://tieba.baidu.com/p/5933861133?pn='+str(i)
        list_url.append(url_)
    return list_url


def get_content(urls):
    for url in urls:
        html = requests.get(url=url, headers=headers).text
        s = etree.HTML(html)
        file = s.xpath('//*[@id="j_p_postlist"]/div/div[2]/div[1]/cc/div/text()')
        for i in file:
            if len(i) < 20 and '如果' in i and '我就' in i:
                i = i.lstrip().rstrip()
                save_content(i)
                print(i)

        time.sleep(1)

def save_content(text):
    with open('ig冲鸭.txt','w+',encoding='utf-8') as f:
        f.write(text)

def main():
    url = 'https://tieba.baidu.com/p/5933861133?pn=1'
    html = requests.get(url=url,headers=headers).text
    s = etree.HTML(html)
    # 获得帖子的总页数
    page = s.xpath('//*[@id="thread_theme_7"]/div[1]/ul/li[2]/span[2]/text()')
    page = int(page[0])

    urls = get_urls(page)
    get_content(urls)
    print('数据保存在ig冲鸭.txt')
    t = input('请按任意键退出！')

main()
