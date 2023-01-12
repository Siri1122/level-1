import multiprocessing as mp
import math
import time
from time import time,perf_counter
result1=[]
result2=[]
result3=[]
def calculate_one(number):
    for i in number:
        result1.append(math.sqrt(i**3))
def calculate_two(number):
    for i in number:
        result2.append(math.sqrt(i**5))
numlist=list(range(1200000))
start=perf_counter()
calculate_one(numlist)
calculate_two(numlist)
end=perf_counter()
print(f'{end-start}')
print("hi")
