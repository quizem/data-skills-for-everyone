# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:45:06 2022

@author: kwaby
"""

"""
1. Python Program to Check Whether a Number is Positive or Negative
2. The program takes the upper and lower limit and prints all odd 
numbers within a given range.

3. Python Program to Print All Numbers in a Range Divisible by a Given Number
4. Python Program to Count the Number of Digits in a Number


"""

#1.
x = int(input("Please enter a number: "))
check = 0
if x > check:
    print('input is positive')
else:
    print('input is negative')
    

#2. The program takes the upper and lower limit and prints all odd numbers
lower_limit = int(input("Please enter the lower limit: "))
upper_limit = int(input("Please enter the upper limit: "))
numbers = list(range(lower_limit,upper_limit))


for number in numbers:
    if number%2 != 0 :
        print(number," is odd")
        #print(number," is even")
    
    # else:
    #     print(number," is odd")
    
    























