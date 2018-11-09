import requests
import json
import time
from lxml import etree




'''
1.获取所有question的id
2.根据id获得回答，回答数，回答者的信息，评论
3.根据评论获取评论者信息

'''

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
}



# 获取所有问题的id
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


# 获取所有评论的url
def get_urls(id,pn):
    urls = []
    pn = int(pn)//5+1
    for i in range(pn):
        i = i * 5
        url = 'https://www.zhihu.com/api/v4/questions/' + str(
            id) + '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=' + str(
            i) + '&sort_by=default'
        urls.append(url)
    return urls


# 获取pn
def get_pn(id):
    list_pn = []
    for i in id:
        url = 'https://www.zhihu.com/question/'+str(i)
        html = requests.get(url, headers=headers).text
        s = etree.HTML(html)
        pn = s.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div[1]/h4/span/text()') #获得每个问题的回复数
        list_pn.append(pn)
    return list_pn

# 输出评论
def print_content(urls):
    url_ = urls[0]
    question = requests.get(url_,headers=headers).json().get('data')
    print("{} {}".format('question:',question[0].get('question')['title']))
    for url in urls:
        items = requests.get(url,headers=headers).json().get('data')
        for item in items:
            outline = item.get('excerpt')
            author = item.get('author')['name']
            url_token = item.get('author')['url_token'] # 匿名用户的信息获取不到
            headline,work =  get_info(url_token)
            print("{} {} {} {}".format('回答者:',author,'回答:', outline))
    time.sleep(1)

# 获取个人信息
def get_info(url_token):
    url = 'https://www.zhihu.com/people/'+str(url_token)+'/activities'
    html = requests.get(url, headers=headers).text
    s = etree.HTML(html)
    headline = s.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[2]/text()')[0]
    # place = s.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/text()')
    work = s.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/text()')[0]
    # intro = s.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/div/div/div')
    # print("{} {}".format(headline,work))
    return headline,work

# id = 32017085
# url = 'https://www.zhihu.com/question/32017085'
# html = requests.get(url, headers=headers).text
# s = etree.HTML(html)
# pn = s.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div[1]/h4/span/text()')[0]
# print(pn)
# urls = get_urls(pn)
# print_content(urls)
# url_token = 'tnt-freedom'
# get_info(url_token)

def main():
    offset = 3
    id = get_id(offset)
    # print(id)
    for i in id:
        pn = get_pn(i)
        print(pn)
        # urls = get_urls(i,pn)
        # print(urls)


main()