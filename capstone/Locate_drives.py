# import string
# import win32api
# import os
# drives = win32api.GetLogicalDriveStrings()
# print(drives)
# drives = drives.split('\000')
# print(drives)
# import os
# d="C:\HCL"
# di={}for root,dir,files in os.walk(d):
    #  for d in dir:
       # di[d]=os.listdir(root+"/"+d)
# print(di)
# import multiprocessing as mp
# print("Number of processsors: ",mp.cpu_count())