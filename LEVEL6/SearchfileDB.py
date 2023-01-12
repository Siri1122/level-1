import sqlite3
class SearchDB():
    def __init__(self):
        self.connect = sqlite3.connect("c://sqlite//hcl.db")
        self.cur = self.connect.cursor()
    def searchDB(self, fil):
        self.f="filename"
        sql="""select * from filelog where filename like '%{0}'""".format(fil)
        self.cur.execute(sql)
if __name__=='__main__':
    dbObj=SearchDB()
    print(dbObj.connect)
    print(dbObj.cur)



