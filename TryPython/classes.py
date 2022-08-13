# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 08:23:03 2022

@author: kwaby

Scenario: we want to analyze test results for students in a class
"""
# calculate average grades
# generate grade letter for each of the scores

students={
    'John':[50,80,89],
    'Paul':[89,76,100],
    'Nelson':[78,90,67]
    }


def average(grades):
    return  sum(grades)/len(grades)


for grades in students.values():
    #average
    #ave = sum(grades)/len(grades)
    print(average(grades))




class Student():
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
        
    
    def take_exam(self,name):
        pass
    
# Scenario 2: OPD
# People: 
    
# track patients
patient_name =''
patient_age =0


# doc
doc_name =''
doc_specialty=''
doc_assigned_room=''

def assign_room_to_doc(doc,room_no):
    pass
















