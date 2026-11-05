# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:51:09 2026

@author: Naziri
"""

# Taklif 4

purchase_amount=float(input('enter your purchase amount in Toman:'))

if  purchase_amount>10000000:
    print('shipping cost is free')
    
elif purchase_amount>500000:
    
    print('shipping cost is 30000 toman')
    
elif purchase_amount>0:
      
      print('shipping cost is 60000 toman')  