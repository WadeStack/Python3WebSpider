import os
import re
import shutil
import requests

keyword = input("请输入需要下载的图片关键字: ")
j = int(input('请输入需要爬取的图片页数(一页60张):'))

#获取该网页的源码    
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

#创建一个关键字的文件夹
def create_file(keyword):
    if os.path.exists(keyword):
        shutil.rmtree(keyword)
        os.makedirs(keyword)
    else:
        os.makedirs(keyword)

#下载图片
def download_picture(html):
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    print ('找到关键词:'+keyword+'的图片，现在开始下载图片...')
    i = 0
    count = 0
    while(count < j):
        for pic_url_ in pic_url:
            print ('正在下载第'+str(i+1)+'张图片')
            try:
                html_= requests.get(pic_url_, timeout=10)
            except requests.exceptions.ConnectionError:
                print ('【错误】当前图片无法下载')
                continue
            string = keyword + '\\' + keyword + '_'+str(i) + '.jpg'
            fp = open(string,'wb')
            fp.write(html_.content)     # 将图片的二进制数据写入到文件中
            fp.close()
            i += 1
        count += 1
    print('下载完成!!!')


def main():
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+ keyword
    html = get_one_page(url)
    create_file(keyword)
    download_picture(html)

main()
