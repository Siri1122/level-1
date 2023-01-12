import multiprocessing as mp
from capstone.level1 import find
from time import perf_counter
from threading import Thread
def search():
    find(name,path)
start_time=perf_counter()
name=input("enter the name of the file")
path=input("enter the path")
t1=Thread(target=search)
t1.start()
t1.join()
print("Number of processors:",mp.cpu_count())
end_time=perf_counter()
print(f"{end_time-start_time} seconds taken")