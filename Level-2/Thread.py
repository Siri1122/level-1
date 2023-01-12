from time import perf_counter
from threading import Thread
from capstone.level1 import find
start_time=perf_counter()
name=input("enter the file name ")
path=input("enter the path")
t2=Thread(target=find(name,path))
t2.start()
t2.join()
end_time=perf_counter()
print(f'{end_time-start_time} seconds return')