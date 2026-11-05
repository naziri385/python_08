# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:01:05 2026

@author: Naziri
"""

# Taklif 5

password=input('enter your password:')

if  len(password)<8:
    print('password length is short')
    
if password.isdigit() :
    
    print('password is only contain number')
    
if password.strip() :
    
    print('there is distance between your coracters')
    
 #============================================================
   
password=input('enter your password:')

if  len(password)<8:
      print('password length is short')
      
elif password.isdigit() :
      
      print('password is only contain number')
      
elif password.strip() :
      
      print('there is distance between your coracters')  
    
