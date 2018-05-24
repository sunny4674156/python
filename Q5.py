# -*- coding: utf-8 -*-
"""
題目：

請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式 compute()，
此函式接收兩個參數a,b，並回傳a的b平方的數值

"""

A = int(input("輸入第一個數字："))
B = int(input("輸入第二個數字："))
print("第一數：",A)
print("第二數：",B)

def compute(A,B):
    C=A**B
    return C
x=compute(A,B)
print(A,"的",B,"平方，結果為：",x)








    

    
