import requests
import json
import time


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
}

# 获取热评的前50的url
def get_urls(id):
    urls = []
    for i in range(10):
        i = i * 5
        url = 'https://www.zhihu.com/api/v4/questions/' + str(id) + '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=' + str(i) + '&sort_by=default'
        urls.append(url)
    return urls

# 输出神评
def print_content(urls):
    url_ = urls[0]
    question = requests.get(url_,headers=headers).json().get('data')
    print("{} {}".format('question:',question[0].get('question')['title']))
    for url in urls:
        items = requests.get(url,headers=headers).json().get('data')
        for item in items:
            outline = item.get('excerpt')
            if len(outline) < 50 and item.get('voteup_count') > 388:
                print("{} {}".format('answer:',outline))
        time.sleep(1)



def main():
    id = input('请输入问题的url:')
    id = id.split('/')  # 字符串切片
    id = id[-1]         # 取倒数第一个切片
    list_url = get_urls(id)
    print_content(list_url)

main()
