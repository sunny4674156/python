# -*- coding: utf-8 -*-
"""
題目：

請撰寫一程式，讓使用者輸入一個正整數，將正整數以反轉順序輸出，
並判斷如輸入的正整數為0，則輸出為0

"""

list=[]
A = 0
while 2>1:
    A=int( input("請輸入整數(輸入0即輸出為0):"))
    
    if A == 0:
        break
    
    list.append(A)
    
    print("即時輸入串列內容：",list)
print("原輸入串列-->",list)
print("反轉的內容(▼越小)：")
l=len(list)
i=0
while i<l:
    list2=list.pop()
    print(list2)
    i=i+1







    

    
