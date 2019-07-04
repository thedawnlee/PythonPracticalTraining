#day10（爬虫基础）
    
    
    所需包：
    requests
    beautifulsoup4
    
<h3>爬虫起因：
        
        数据从何而来？
        企业产生的用户数据
        数据平台购买数据
        政府机构公开的诗句
        数据管理咨询公司：麦肯锡
        爬取网络数据
        
        里程碑：google底层采用python
        
        爬虫分类：通用爬虫  聚焦爬虫
        
        通用爬虫：谷歌 百度 搜索引擎
        
<h3>数据存储：

        将数据存在原始页面数据库，页面数据与用户浏览器得到的html是完全一致的
        
<h3>预处理：

        提取文字
        中文分词
        消除噪音
        链接关系计算
        特殊文件处理
        
<h3>提供检索服务，网站排名

        搜索引擎对信息进行组织和处理之后，为用户提供关键字服务，将用户检索相关信息展示给用户。

<h3>爬虫常用库
        
        requests
        urllib2
        urllib2
        scrapy

<h3>步骤

        获取网页内容
        进行处理展示




<h4>requests库概述
        
        建立在urllib3库基础上进行的更友好的函数方式
        支持非常多的链接访问功能
        帮助网站：http：//doc.python-requests.org
        

<h2>beautifulsoup4
        
        beautifulsou4根据html与xml根据语法来构建成树的形式
<h2>爬虫案例：中国大学排名

        import requests
        from bs4 import BeautifulSoup
        import Db_Util as db
        
        conn = db.DBUtil(password='12345', databasename='rkrank')
        def get_data_to_db():
            r  = requests.get("http://www.zuihaodaxue.cn/subject-ranking/computer-science-engineering.html")
        
            r.encoding='utf-8'
            soup = BeautifulSoup(r.text)
            list_university = []
            for i in range(len(soup.find_all('td'))):
                list_university.append(str(soup.find_all('td')[i].string))
        
            for i in range(0,len(list_university),9):
                c = list_university[i:i+9]
                conn.insetOne("insert into rkRank02 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",c)
        
        
        def print_data():
            res = conn.Listall(tablename='rkrank01')
            print("{:^10}\t{:<20}\t{:^10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}".format('排名','名称','综合得分','论文分数','论文标准化影响力','国际合作论文比例','顶尖期刊论文数','教师获权威奖项数'))
            for param in range(len(res)):
                print("{:^10}\t{:<20}\t{:^10}\t{:^20}\t{:^10}\t{:>10}\t{:>20}\t{:>20}".format(res[param][0],res[param][1],res[param][2],res[param][3],res[param][4],res[param][5],res[param][6],res[param][7]),end="")
                print("\n")
            conn.db.close()
            conn.cursor.close()
        
        
        print_data()
        
        # get_data_to_db()

        
        
        
Date：2019.06.18  
Author:Dawn  
Location:Jinan   
Wechat：llmllm_llm  
[新浪微博](https://weibo.com/u/5034954422)
 
![blockchain](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=702257389,1274025419&fm=27&gp=0.jpg "区块链")

        
        