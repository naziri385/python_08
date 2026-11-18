# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:03:12 2026

@author: Naziri
"""
# Taklif L5

# Tamrin 1 ================


for i in range(11,50,2):
  
    print(i)
    
  
#Tamrin 2 =================


for i in range(20,0,-1):
      print(i)
            

#Tamrin3=====================   


total=0
    
for i in range (1,101):
    
    total+=i
    
print('total sum=',total) # baray inke faghat print halgheh anjam bedeh print ra az halgheh biron mibrim
    
#Tamrin 4 =================

number = int(input("Enter an number: "))

for i in range(1, 11):
    
  
    
 print(f"{number} x {i} = {number * i}")
    
# Tamrin 5===================

numbers=[12,7,25,18,3,40,11,8] 

even_number=[]
count=0

for i in numbers:
    
    if i%2 ==0:
        
        print(i)
        
        count+=1
        even_number.append(i)
print('count=',count)
print(even_number)
        

       
# Tamrin 6===================  

score=[15,18,12,20,16,14,19] 

total=0

for number in score:
    
    total+=number

print('average=',total/len(score)) # 16.28571428


print('total',total) #114


# Tamrin 7=================== 
 
numbers=[2,4,6,8,10]

squre=[]

for i in numbers:
    
   squre.append(i**2)
      
print(squre)       

# Tamrin 8 =================== 
       
number=int(input('how many number do you want to enter?'))

list_number=[]

for i in range(0,number):
    
     new_number=int(input('enter your  number?'))
    
     list_number.append(new_number)
    
print(list_number)    

# Tamrin 9 =================== 

numbers=[4, 9, 15, 23, 42, 56, 71]

target=int(input('number'))

found=0
for number in numbers :
    if number==target:

        print('number found')
        
        found=1
        
        break
if found==0:
        print('number not found')
        
# Tamrin 10 ===================

for number in range(1,31):
    
   if number % 3 == 0:
          
      print(number)
    
# Tamrin 11 ===================

total=0

for number in range(0,10):
    
    new_number=int(input('enter number'))
    
    if new_number == 0 :
        break
    total+= new_number
    print(total)
    
# Tamrin 12 ===================

students=[("Ali", 22),("Sara", 19),("Reza", 25),("Nima", 20),("Mina", 23)]

for name,age in students:
    
    print('name :',name,',','age :',age)
    
# Tamrin 13 ===================  

students=[("Ali", 18),("Sara", 12),("Reza", 9),("Mina", 20),("Nima", 14)] 

for name,score in students :
    
        if score>15:
    
          print(name)
          

# Tamrin 14 ===================  

products=[("Laptop", 50000, 2),("Mouse", 800, 3),("Keyboard", 1500, 2),("Monitor", 12000, 1)]

total=0

for name,price,quantity in products:
    
    subtotal=price*quantity
    
    print(subtotal)
    
    total+=subtotal
    
    print(total)
   
# Tamrin 15 ===================

users=[(1, "ali", "active"),(2, "sara", "inactive"),(3, "reza", "active"),(4, "mina", "inactive"),(5, "nima", "active")]

target=input('username')

found=0

for user_id,username,status in users:
    
    if username== target:
        print(user_id,username,status)
        
        found=1
        break
    if found==0:
        print('user not found')



    
    
    
    