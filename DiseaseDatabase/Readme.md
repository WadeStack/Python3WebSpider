# 爬取的目标: [疾病资料库](http://web.tfrd.org.tw/genehelp/diseaseDatabase.html?selectedIndex=0)
    
# 过程中的难点: 
1. 对网页源码的数据清洗:re.sub()
2. csv存储数据
  2.1 [补充csv乱码的解决](https://blog.csdn.net/Code_7900x/article/details/83099456)

# 第二次更改:
网页源码为JSON格式,这就大大简化了数据处理,就不用再考虑单引号和制表符的问题
