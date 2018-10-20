from wxpy import *
import jieba
import re
from snownlp import SnowNLP
import jieba.analyse
import matplotlib.pyplot as plt

bot = Bot(console_qr=True, cache_path=True) # 登陆一次后利用缓存登陆
# bot =Bot() # 每次都需要登陆
friends = bot.friends()

# 总体分析
def analyseTotal(friends):
    result = friends.stats_text()
    print(result)

# 具体分析每个好友
def analyseConcrete(friends):
    text = friends.stats()
    print('sex:',text['sex'])
    print('province:',text['province'])
    print('city:',text['city'])
    for friend in friends[1:]:
        print(friend.name,friend.sex,friend.province,friend.city,friend.signature)

# 性别分析,饼状图显示
def analyseSex(friends):
    text = friends.stats()
    male = text['sex'][1]
    female = text['sex'][2]
    unknown = text['sex'][0]
    labels = 'male','female','unknown'
    sizes = [male,female,unknown]
    explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# 分析个性签名
def analyseSignature(friends):
    signatures = ''
    emotions = []
    pattern = re.compile("lf\d.+")
    for friend in friends[1:]:
        signature = friend.signature
        if signature != None:
            signature = signature.strip().replace('span','').replace('class','').replace('emoji','')
            signature = re.sub(r'lf(\d.+)','',signature)
            # print(signature)
            if len(signature) > 0:
                nlp = SnowNLP(signature)
                emotions.append(nlp.sentiments)
                signatures += ''.join(jieba.analyse.extract_tags(signature,5))
    # with open('signatures.txt', 'wt', encoding='utf-8') as file:
    #     file.write(signatures)
    # Signature Emotional Judgment
    count_good = len(list(filter(lambda x: x > 0.66, emotions)))
    count_normal = len(list(filter(lambda x: x >= 0.33 and x <= 0.66, emotions)))
    count_bad = len(list(filter(lambda x: x < 0.33, emotions)))
    labels = [u'负面消极', u'中性', u'正面积极']
    values = (count_bad, count_normal, count_good)
    plt.rcParams['font.sans-serif'] = ['simHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel(u'情感判断')
    plt.ylabel(u'频数')
    plt.xticks(range(3), labels)
    plt.legend(loc='upper right', )
    plt.bar(range(3), values, color='rgb')
    plt.title(u'%s的微信好友签名信息情感分析' % friends[0])
    plt.show()

def main():
    analyseTotal(friends=friends)
    # analyseConcrete(friends=friends)
    analyseSex(friends=friends)
    analyseSignature(friends=friends)
    x = input('输入任意字符退出')

main()


