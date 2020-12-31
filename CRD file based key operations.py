import threading 
from threading import*
import time
d={}
l=[]
def create():
    print("Enter the key value pair to add\n")
    key,value=map(str,input().split())
    key=int(key)
    print("Time-To-Live property(Time in minutes)\n")
    ti=int(input())
    ti=ti*60
    if key in d:
        print("Error: this key is Already exists:\n")
    else:
        if len(d)<(1024*1024*1024) and key<(16*1024*1024):
            if ti==0:
                l=[value,ti]
            else:
                l=[value,time.time()+ti]
            if len(value)<=32:
                d[key]=l
                print("Successfully Created\n")
            else:
                print("Error: Invalid Key value\n")
        else:
            print("Error: Memory Limit exceed\n") 
                
def read():
    print("Enter key to read the pair\n")
    key=int(input())
    if key not in d:
        print("Error: Key does not Exist\n")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                res=str(key)+":"+str(b[0])
                print(res)
            else:
                print("Error: time to live expired\n")
        else:
            res=str(key)+":"+str(b[0])
            print(res)
def delete():
    print("Enter the key to delete\n")
    key=int(input())
    if key not in d:
        print("Error: Key does not Exist\n")
    else:
        del d[key]
        print("Successfully deteled\n")

print("File based key-value data store\n")
i=1
while(i!=5):
    print("Select the operation you want to do:\n")
    print("1-Create\n2-Read\n3-Delete\n4-Show all\n5-Exit\n")
    opt=int(input())
    if(opt==1):
        create()
    elif(opt==2):
        read()
    elif(opt==3):
        delete()
    elif (opt==4):
        print(d)
    elif(opt==5):
        i=5
    else:
        print("Invalid Operation\n")
print(d)
t1=Thread(target=(create or read or delete)) 
t1.start()
time.sleep(1)
t2=Thread(target=(create or read or delete))
t2.start()
time.sleep(1)

f=open("crd.txt",'w')
strc=str(d)
f.write(strc)
f=open("crd.txt",'r')
print(f.read())
f.close()
