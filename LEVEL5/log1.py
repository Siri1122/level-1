# import re
# import logging
# class searchlog():
#     def __init__(self):
#         logging.basicConfig(filename="filelog1.txt",level=logging.INFO)
#     def dbsearchlog(self,filename):
#         file=open("file1.txt","r")
#         str="text_file1"
#         data=re.compile(str)
#         res=data.search(str)
#         line=file.readline()
#         print(res.group(0))

import logging
class Demofile():
    def __init__(self):
        logging.basicConfig(filename="filelog.txt",level=logging.WARNING)
    def Fileopen(self):
        try:
            f=open("text","r")
        except FileNotFoundError as msg:
            logging.exception(msg)
if __name__=='__main__':
    obj=Demofile()
    obj.Fileopen()