import win32api
import os
drives = win32api.GetLogicalDriveStrings()
print(drives)
drives = drives.split('\000')
print(drives)
def find(filename, path):
    c=0
    for root,dirs,files in os.walk(path):
        for name in files:
            if name==filename:
                c+=1
                print("file is present")
                print(root)
                break
    if(c==0):
        print("file is not present")
        print("path is not present")

dir = "C://"
