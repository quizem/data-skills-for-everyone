# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:11:37 2022

@author: Amo

- boolean expressions
- logical operators
- comparison operators
- conditional excution
- alternative execution
- chained conditionals
- nested conditionals
"""

# logical operators
# and, or, not

# Conditional:
# x>0, x<0,x==0
# x < y, x > y,x == y

y = 10
x = 5


if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x is equal to y')
    

# nested conditionals
if x== y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
        
        
is_infected_with_malaria = True
is_longer_2_weeks = True

if is_infected_with_malaria:
    if is_longer_2_weeks:
        print("oh, we are so sorry for you.")
#          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        