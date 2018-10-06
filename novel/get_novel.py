
import os
import re
import sys
import requests

#定义全局变量keyword,方便创建text
keyword = input('请输入你要下载的小说:')
name = str(keyword) + '.txt'

#获取网页的源码
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

#获取所有章的url
def get_url(html):
    #用正则表达式提取出所需要的部分
    URL = re.findall('<li class="c3"><a href="(.*?)"><span>',html,re.S)
    list_url = []   # 定义一个列表来存储所有章的URL
    for url_ in URL:
        list_url.append( 'http://quanben5.com' + url_ )
    return list_url

#获取单章的内容
def get_content(html):
    title = re.findall('<h1 class="title1">(.*?)</h1>',html,re.S)
    title = title[0]
    print(title + '开始下载')
    write_to_file(title)
    content = re.findall('<p>(.*?)</p>',html,re.S)
    for sentence in content:
        write_to_file(sentence)
    write_to_file('\n')

#将内容保存到本地
def write_to_file(content):
    with open(name,'a',encoding = 'utf-8') as f:
        f.write(content+'\n')

#将所有章节保存到本地
def save_content(list_url):
    for url_ in list_url:
        html_ = get_one_page(url_)
        get_content(html_)


def main():
    url = 'http://quanben5.com/index.php?c=book&a=search&keywords='+keyword
    html = get_one_page(url)
    url1 = re.findall(r'<h3><a href="(.*?)">',html,re.S)
    if url1 == []:
        print('搜索不到!!!')
        flag = input('是否退出:(Y or N):')
        if flag == 'Y':
            sys.exit()
        elif flag == 'y':
            sys.exit()
        else:
            print('搜不到能怎么办,我也很无奈-.-||')
    else:
        url1 = url1[0]  # 获得小说URL
        url2 = 'http://quanben5.com'+url1+'/xiaoshuo.html'  # 获得小说目录页URL
        html2 = get_one_page(url2)
        list_url = get_url(html2)
        print(name + '开始下载!!!')
        save_content(list_url)

main()
