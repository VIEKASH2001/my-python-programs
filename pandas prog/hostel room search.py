import pandas as pd
import numpy as np

p=pd.read_csv('hostel allotment.csv')
r=p['Pairs']
num=r.values
size=num.size
new = []
for i in num:
    new.append(i)
    
m=list(new)
ch='y'
while(ch=='y'):
    ele=input('input the roll.no')
    ele=list(ele)
    n=0
    for i in range(size):
        c=0
        d=0
        j=2
        k=15
        l=m[i]
        for q in range(9):
            if(ele[q]==l[j]):
                c+=1
            j+=1  
            if(ele[q]==l[k]):
                d+=1
            k+=1
        if(c==9 or d==9):       
            print(p[i:(i+1)])
            n+=1
            break
    if(n==0):
        print("you entered an invalid number")
    ch=input('dp ypu want to search another number (y/n)')   

print("service ends !!!!!")
