from sqlconnect.sqlcommon import sqlconnect
import pymysql
class duosql(sqlconnect):
    def __init__(self):
        self.conn=pymysql.connect(host='192.168.202.131',port=3306,user='root',password='mysql',database='school',charset='utf8')
        self.cursor=self.conn.cursor()
if __name__ == '__main__':
#     a=duosql()
#     fetchall=a.query('select * from focus')
#     print(fetchall)

    
    
