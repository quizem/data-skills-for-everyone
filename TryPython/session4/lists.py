# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:01:04 2022

@author: kwaby


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
mylist = []
list('as i go through the lesson')

msg = "hello everyone, how are you doing?"
words = msg.split()

# List methods
# 'append',

mylist.append('new item 1')
mylist.append('new item 2')
mylist.append(123)
mylist.append([100,98,120])


#
student_scores = [50,70,17,60,10,56]
new_scores = []
# add 20 to each score

for score in student_scores:
    #temp = score + 20
    new_scores.append(score + 20)


# 'clear',
# 'copy',
# 'count',
# 'extend',

# we have 2 lists
class_a_scores = [90,60,20,78,30]
class_b_scores = [8,9,10,11]


class_a_scores.extend(class_b_scores)

# appending a list to a list
class_a_scores.append(class_b_scores)
# combined_scores = class_a_scores.append(class_b_score)


# 'index': find the index of an item in the list


# 'insert',
class_a_scores.insert(0,100)
# 'pop',

class_a_scores.pop()
# 'remove',

class_a_scores.remove(20)
# 'reverse',
class_b_scores.reverse()
class_b_scores.reverse()
# 'sort'

# lists and built-in functions:

max(class_b_scores)
min(class_b_scores)

class_a_max, class_b_min = max(class_b_scores),min(class_b_scores)


a,b = class_a_scores[0],class_a_scores[-1]

