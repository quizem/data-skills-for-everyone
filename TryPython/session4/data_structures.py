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
- Loops
- Introduction to data structures
"""

students = ['Ed','Amo','Anita','Jon'] # 0 based
numbers = [1,2,3,4,5]
colection = ['persona',1,1.5,0]

# tables: name, age, sex, class
csv = [
      
       ['Paul',12,'M',4],
       ['Ed',10,'M',3],
       ['Jerry',11,'M',3],
      ]

average = 0
for student in csv:
    average = average + student[1]

average/len(csv)
# pull out a single student

first_student = ['Paul',12,'M',4]

print(first_student[0])
print(first_student[1])
print(first_student[2])
print(first_student[3])
# display each item in the csv variable

for student in csv:
    print(student[0])
    
    
# collect all names in one variable
names_list = []

for student in csv:
    names_list.append(student[0])



# collect all ages in one variable
ages = []
for student in csv:
    ages.append(student[3])



# a very tall list

a_tall_list = list(range(100))
len(a_tall_list)


# sum all the numbers in this list
a_tall_list[0]+a_tall_list[1]+a_tall_list[3]

# a nice way to sum
total = 0

for number in a_tall_list:
    total = total + number
    print(total)
























