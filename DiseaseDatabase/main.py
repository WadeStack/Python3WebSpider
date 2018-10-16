import re
import csv
import time
import requests
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

def main():
    u = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
         'O','P','Q','R','S','T','U','V','W','X','Y','Z','CD']
    print('开始下载数据:')
    for i in u:
        url = 'http://web.tfrd.org.tw/genehelpDB/GeneHelp/DiseaseDBIndex/' + str(i)
        print('开始下载'+i)
        html = requests.get(url, header).text
        # 清洗数据
        html = re.sub(r'\\t', '', html) # 除去制表符\t
        html = re.sub(r'\\', "'", html) # 除去\
        html = re.sub(r'u0027', '', html) # 除去u0027(一次除去\u0027太难了)

        Type = re.findall(r'"index":"(.*?)"',html)
        nameEN = re.findall(r'"nameEN":"(.*?)"',html)
        nameCH = re.findall(r'"nameCH":"(.*?)"',html)

        # 存储数据
        with open('data.csv', 'a', encoding='utf-8')as csvfile:
            writer = csv.writer(csvfile)
            for type_,nameE, nameC in zip(Type,nameEN,nameCH):
                if '問答集' not in nameC and '訊息' not in nameC and '相關' \
                        not in nameC and '友善團體' not in nameC and '說明' not in nameC:
                    print(type_, nameE, nameC)
                    writer.writerow([type_,nameE,nameC])
        time.sleep(1)

    print('生成文件data.csv')
    e = input('输入任意字符结束程序!')

main()







