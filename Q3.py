# -*- coding: utf-8 -*-
"""
題目：

請輸入迴圈敘述寫一程式，讓使用者輸入一個正整數a，
利用迴圈計算從1到a之間，所有5之倍數數字之總和

"""

s = 0
A = int(input("請輸入正整數："))
print("所輸入的正整數為：",A)

for i in range(1,A+1):
    if i % 5  == 0:
        s=s+i
        
print("5的倍數總和：",s)






    

    
