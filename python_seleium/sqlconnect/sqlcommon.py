import pymysql
class sqlconnect():
    def __init__(self,host,port,user,password,database,charset):
        self.conn = pymysql.connect(host,port,user,password,database,charset)
        self.cursor=self.conn.cursor()
    def countQuery(self,sql):
        row_count = self.cursor.execute(sql)
        return row_count
    def query(self,sql):
        execute=self.cursor.execute(sql)
        #获取数据
        fetchall=self.cursor.fetchall()
        #获取列名
        index=self.cursor.description
        result=[]
        for res in fetchall:
            row={}
            for i in range(len(index)):
                row[index[i][0]]=res[i]   
            result.append(row)
        return result
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        