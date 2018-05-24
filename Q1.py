# -*- coding: utf-8 -*-
"""
題目：

請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a,b，然後再輸入
一算術邏輯子(+,-,*,/,//,%)，輸出這兩個數以及其經過運算後的結果

"""

A = int(input("請輸入第一個數字："))
B = int(input("請輸入第二個數字："))
C = str(input("請輸入算術運算子："))
print("第一個數字為：", A)
print("第二個數字為：", B)
print("算術運算子為：", C)

if  C == "+" :
    Ans= A+B
elif  C == "-" : 
    Ans = A-B
elif  C == "*" : 
    Ans = A*B
elif  C == "/" : 
    ans = A/B

elif  C == "//" : 
    Ans = A//B
    
elif  C == "%" : 
    Ans = A%B 
print("答案：", Ans)










    

    
