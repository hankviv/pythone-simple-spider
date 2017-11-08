import pymysql
class store:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', db='renrenche', charset='utf8')

    def store_list(self,res):
        while len(res) >0:
            print(len(res))
            item = res.pop()
            cursor = self.conn.cursor()
            cursor.execute("insert into car_list values(%s, %s, %s, %s, %s)",item)
        self.conn.commit()
        cursor.close()
        return True
    def store_detail(self):
        return True



#a = store()
#a.store_list([1,2,3,4,5])