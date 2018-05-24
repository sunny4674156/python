# -*- coding: utf-8 -*-
"""
題目：

請撰寫一程式，輸入一圓半徑，並加以計算此圓之面積和周長
最後請印出此圓的半徑、面積、周長

*提示：輸出浮點數到小數點第二位

"""

import math  

A = eval(input("請輸入圓半徑："))
print("圓半徑= %.2f"  %  A )
B = (2*A)*math.pi
print("圓周長： %.2f"  %  B)
C = A*A*math.pi
print("圓面積： %.2f"  %  C)











    

    
