"""
TO DO
======
The focus of the tutorial will not be on the data generation so I will
not recod the data generation steps or I can include it for additional 
bonus:

    1. Data genetation
    2. Setting up template
    3. Generate pdf
    4. Optional styling
    5. Automate report generation


Refs:
    https://en.wikipedia.org/wiki/Academic_grading_in_the_United_States#Rank-based_grading
"""
#===================== IMPORTS ===============================================
import os
import openpyxl
import pandas as pd
from faker import Faker
from pathlib import Path
import numpy as np

from jinja2 import Template


#===================== GENERATE DATA ========================================
# We fake some class data from the normal distribution


class_averages = {
    'math': 65,
    'physics':70,
    'chemistry': 59,
    
    }
number_of_students = 35
sigma = 25


fake = Faker()

names = np.array([fake.name() for i in range(number_of_students)])


math_grades = np.round(np.random.normal(loc = class_averages['math'],
                               scale = sigma,
                               size = number_of_students),1)

physics_grades = np.round(np.random.normal(loc = class_averages['physics'],
                               scale = sigma,
                               size = number_of_students),1)

chem_grades = np.round(np.random.normal(loc = class_averages['chemistry'],
                               scale = sigma,
                               size = number_of_students),1)

df = pd.DataFrame(zip(names,math_grades,physics_grades,chem_grades),
                  columns=['name','math','physics','chemistry'])



# Grade Convertion
#bins = pd.IntervalIndex.from_tuples([(0,59),(60,69),(70,79),(80,89),(90,100)])
bins = [0,59,60,70,80,90,100]
grade_labels = ['F','E','D','C','B','A']
gpa = [0.0,1.0,2.0,3.0,4.0]

def get_grade_letter(grade):
    if grade <=59.0:
        return 'F'
    elif grade > 59.0 and grade < 69.0:
        return 'D'
    elif grade > 69.0 and grade < 79.0:
        return 'C'
    elif grade > 79.0 and grade < 89.0:
        return 'B'
    elif grade > 89.0:
        return 'A'
    
#===================== 1. LOAD DATA ==========================================
DATA_FOLDER = Path(r".\data")

#=================== 3. A SIMPLE TEMPLATE =============================================
template = """
    =========== REPORT CARD =============
                {student}
    Subject  | Score | Grade | GPA
    -------------------------------
    Math      {math_score:^7} {math_grade:^7} {math_gpa:^6}
    Physics   {phy_score:^7} {phy_grade:^7} {phy_gpa:^6}
    Chemistry {chem_score:^7} {chem_grade:^7} {chem_gpa:^6}
"""

template = """
    =========== REPORT CARD =============
                {student}
    Subject  | Score | Grade | GPA
    -------------------------------
    Math      {math_score:^7} {math_grade:^7} {math_gpa:^6}
    Physics   {phy_score:^7} {phy_grade:^7} {phy_gpa:^6}
    Chemistry {chem_score:^7} {chem_grade:^7} {chem_gpa:^6}
"""


records = df.to_dict(orient='record')

one_person_str = ''
record =records[0]
student = record.pop('name')

subject_dict = {}
subject_dict['student'] = student
subject_dict['math_score'] = record['math']
subject_dict['phy_score'] = record['physics']
subject_dict['chem_score'] = record['chemistry']

subject_dict['math_grade'] = get_grade_letter(record['math'])
subject_dict['chem_grade'] = get_grade_letter(record['chemistry'])
subject_dict['phy_grade'] = get_grade_letter(record['physics'])

subject_dict['math_gpa'] = 4.0
subject_dict['chem_gpa'] = 4.0
subject_dict['phy_gpa'] = 2.7
subject_dict['total_gpa'] = 2.7



#record['grade'] = get_grade_letter(record['score'])

out=template.format(**subject_dict)
print(out)

with  open(r'.\template.html','r') as fl:
    tp = Template(fl.read())

with open('htmlout.html','w') as file:
    file.write(tp.render(subject_dict))

#=================== 4. A BETTER TEMPLATE  ========================



# take each row in the df and format it as a dict
#=================== 4. CONFIGURE WORD CLOUD SETTINGS ========================



#=================== 5. SAVE TO PDF  ===================================

import pdfkit
pdfkit.from_string(out,'out.pdf')

# Automate everything we have done


def automate(source,destination):
    pass
    

import argparse
import configparser
if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('-s','--source',type=str,help='source folder',default=r'.\data')
        parser.add_argument('-o','--output',type=str,help='output folder',default=r'.\output')
        
        parser.add_argument('--config', '-c', type=argparse.FileType('r'),help='config file')
        args = parser.parse_args()
        
        if args.config:
            config = configparser.ConfigParser()
            config.read_file(args.config)
            args.source = config['ARGUMENTS']['source_folder']
            args.output = config['ARGUMENTS']['output_folder']
            
        automate(args.source,args.output)




























