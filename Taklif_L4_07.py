# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:16:53 2026

@author: Naziri
"""

# Taklif 7

numb1 = float(input('entre your first number:'))
numb2 = float(input('entre your second number:'))
operation = input('which function do you want (addition,subtraction,division,multiplication):')

if operation=='addition':
    print(numb1+numb2)
elif operation=='subtraction':
    print(numb1 - numb2)
elif operation=='multiplication':
    print(numb1 * numb2)
elif operation =='division':
    print(numb1 / numb2)
else:
    print('your have to select one of these operation:addition,subtraction,division,multiplication')
