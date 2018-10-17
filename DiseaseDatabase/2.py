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
        items = requests.get(url, header).json().get('resultString')
        for item in items:
            index = item.get('index')
            nameC = item.get('nameCH')
            nameE = item.get('nameEN')

            # 存储数据
            with open('data.csv', 'a', encoding='utf-8')as csvfile:
                writer = csv.writer(csvfile)
                if '問答集' not in nameC and '訊息' not in nameC and '相關' \
                        not in nameC and '友善團體' not in nameC and '說明' not in nameC:
                    print(index, nameE, nameC)
                    writer.writerow([index,nameE,nameC])

        time.sleep(1)

    print('生成文件data.csv,请打开查看!')
    e = input('输入任意字符结束程序!')

main()







