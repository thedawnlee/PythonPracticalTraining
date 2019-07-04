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
