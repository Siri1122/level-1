import multiprocessing as mp
from capstone.level1 import find
from time import perf_counter
def search_file(name,path):
    find(name,path)
if __name__=='__main__':
    start_time=perf_counter()
    print("Number of processors:",mp.cpu_count())
    name=input("enter the file name:")
    path=input("enter the path:")
    p1=mp.Process(target=search_file,args=(name,path))
    p1.start()
    p1.join()
    end_time=perf_counter()
    print(f'{end_time-start_time} seconds taken')