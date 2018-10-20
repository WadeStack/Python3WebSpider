实现功能:
二维码扫码登陆web版微信
分析好友信息:性别,姓名,位置
- [blog](https://blog.csdn.net/Code_7900x/article/details/83214421)
- [wxpy开发者文档](https://wxpy.readthedocs.io/zh/latest/bot.html)
- [绘制饼状图](https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py)
- [jieba分词](https://github.com/fxsjy/jieba)
- [SnowNLP开发者文档](https://github.com/isnowfy/snownlp)

步骤:
1. 模拟登陆微信web版
2.  获取需要的数据
3.  对数据进行分析

所需第三方模块:

*  [wxpy]( https://wxpy.readthedocs.io/zh/latest/chats.html#): 微信网页版接口封装Python版本，在本文中用以获取微信好友信息
*  [jieba](https://github.com/fxsjy/jieba):  结巴分词的 Python 版本，在本文中用以对文本信息进行分词处理
* [snownlp](https://github.com/isnowfy/snownlp): 一个 Python 中的中文分词模块，在本文中用以对文本信息进行情感判断。
* [matplotlib](https://matplotlib.org/): Python 中图表绘制模块，在本文中用以绘制柱形图和饼图

1. 登陆网页版微信:

```
from wxpy import *
# 初始化机器人，扫码登陆
# bot = Bot()
bot = Bot(console_qr=True, cache_path=True) # 保留缓存自动登录
```
2. 获取数据

```
friends = bot.friends()
```
返回的friends对象是一个包含当前用户的集合.所以取数据的时候采用friends[1:]
好友的数据包括remark_name备注名称,sex性别,province省,city市, signature签名,headimage头像
这次我只分析了前面的name,sex,province,city,signature

3. 数据分析
    3.1 总体分析
	

```
# 总体分析
def analyseTotal(friends):
    result = friends.stats_text()
    print(result)
```

   3.2 具体分析
```
def analyseConcrete(friends):
    text = friends.stats()
    print('sex:',text['sex'])
    print('province:',text['province'])
    print('city:',text['city'])
    for friend in friends[1:]:
        print(friend.name,friend.sex,friend.province,friend.city,friend.signature)
```
   3.3 对性别分析
```
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
```
 
   3.4 对签名进行分析
```
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
```
最后贴个[完整代码](https://github.com/wwt-5/Python3WebSpider/blob/master/wx/TypeInfo/GetInfo.py)
