import os
import threading
class FileSearcher(threading.Thread):
    def __init__(self):
        self.drive = ""
        self.file_name = ""
    def search_for_file(self,drives,file_name):
        try:
            print("This is a search method for file searcher")
            file_paths=[]
            drv=drives+"://"
            print(drv)
            for r,d,f in os.walk(drv):
                for name in f:
                    if name == file_name:
                        print("exists")
                        path = os.path.abspath(os.path.join(r,name))
                        file_paths.append(path)

        except:
            print("there is no error")
        return file_paths
    def run(self):
        self.search_for_file(self.drives,self.file_name)
if __name__=='__main__':
    obj=FileSearcher()
    print(obj.search_for_file("C","program1.txt"))