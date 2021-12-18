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


#===================== GENERATE DATA [OPTIONAL] ========================================
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

def random_grades(average, std, size):
    """
    Generate an array of random number from the normal distribution 
    given a certain average, standard deviation and bumber of items

    Parameters
    ----------
    average : float
        average of the distribution.
    std : float
        spread of the data
    size : int
        number of items in the array

    Returns
    -------
    numpy array

    """
    
    sample = np.random.normal(loc = average, scale = std, size = size)
    return np.round(sample,1)


math_grades = random_grades(average = class_averages['math'], 
                   std = sigma, 
                   size = number_of_students)

physics_grades = random_grades(average = class_averages['physics'], 
                   std = sigma, 
                   size = number_of_students)

chem_grades = random_grades(average = class_averages['chemistry'], 
                   std = sigma, 
                   size = number_of_students)


df = pd.DataFrame(zip(names,math_grades,physics_grades,chem_grades),
                  columns=['name','math','physics','chemistry'])

df.to_csv(Path(r'.\data\records.csv'))



#===================== 1. LOAD DATA ==========================================
DATA_FILE = Path(r".\data\records.csv")
df = pd.read_csv(DATA_FILE)

#===================== 2. PROCESS DATA ==========================================
"""
- Generate a grade letter for each subject based on score obtained
- Generate a GPA for each subject based on score optained
"""

# Grade Convertion
bins = [0,59,69,79,89,100]
grade_labels = ['F','E','D','C','B','A']
gpa = [0.0,1.0,2.0,3.0,4.0]

def get_grade_letter(grade):
    if grade >= 0 and grade <=59.0:
        return 'F'
    elif grade > 59.0 and grade <= 69.0:
        return 'D'
    elif grade > 69.0 and grade <= 79.0:
        return 'C'
    elif grade > 79.0 and grade <= 89.0:
        return 'B'
    elif grade > 89.0:
        return 'A'
    else:
        return 'Please enter a positive number'
    

# Calculate GPA
def calculate_gpa(grade):
    """
    Grade to GPA converter

    Parameters
    ----------
    grade : float
        grade to convert

    Returns
    -------
    float
        GPA of corresponding score

    """
    if grade >= 0 and grade <=59.0:
        return 0.0
    elif grade > 59.0 and grade <= 69.0:
        return 1.0
    elif grade > 69.0 and grade <= 79.0:
        return 2.0
    elif grade > 79.0 and grade <= 89.0:
        return 3.0
    elif grade > 89.0:
        return 4.0
    else:
        return 'Please enter a positive number'
    

def overal_gpa(grades):
    """
    Return over  all gpa for all grades obtained
    """
    
    result = sum(grades)/len(grades)
    return calculate_gpa(result)


#=================== 3. A SIMPLE TEMPLATE =============================================
template = """
    =========== REPORT CARD =============
                {student}
    Subject  | Score | Grade | GPA
    -------------------------------
    Math      {math[score]:^7} {math[grade]:^7} {math[gpa]:^6}
    Physics   {physics[score]:^7} {physics[grade]:^7} {physics[gpa]:^6}
    Chemistry {chemistry[score]:^7} {chemistry[grade]:^7} {chemistry[gpa]:^6}
    
    Total GPA:     {total_gpa:^6}
"""

for row in df.itertuples():
    
    # do this subject by subject
    record_dict = {}
    record_dict['student'] = row.name
    record_dict['math'] = {'score': row.math, 
                             'grade': get_grade_letter(row.math),
                             'gpa': calculate_gpa(row.math)}
    
    record_dict['physics'] = {'score': row.physics, 
                             'grade': get_grade_letter(row.physics),
                             'gpa': calculate_gpa(row.physics)}
    
    record_dict['chemistry'] = {'score': row.chemistry, 
                             'grade': get_grade_letter(row.chemistry),
                             'gpa': calculate_gpa(row.chemistry)}
    
    record_dict['total_gpa'] = round((record_dict['math']['gpa'] + \
                                record_dict['chemistry']['gpa'] + \
                                    record_dict['physics']['gpa'])/3,1)
    
    out=template.format(**record_dict)
    print(out)
    






records = df.to_dict(orient='record')

one_person_str = ''
record =records[0]
student = record.pop('name')

subject_dict = {}
subject_dict['student'] = student
subject_dict['math_score'] = record['math']
subject_dict['math_grade'] = get_grade_letter(record['math'])
subject_dict['math_gpa'] = 4.0

subject_dict['chem_score'] = record['chemistry']
subject_dict['chem_grade'] = get_grade_letter(record['chemistry'])
subject_dict['chem_gpa'] = 4.0

subject_dict['phy_grade'] = get_grade_letter(record['physics'])
subject_dict['phy_score'] = record['physics']
subject_dict['phy_gpa'] = 2.7

subject_dict['total_gpa'] = subject_dict['math_gpa'] + \
                                    subject_dict['math_gpa'] + \
                                    subject_dict['chem_gpa'] + \
                                    subject_dict['phy_gpa']



#record['grade'] = get_grade_letter(record['score'])

out=template.format(**subject_dict)
print(out)

#=================== 4. A BETTER TEMPLATE  ========================
with  open(r'.\template.html','r') as fl:
    tp = Template(fl.read())

with open('htmlout.html','w') as file:
    file.write(tp.render(subject_dict))


#=================== 5. SAVE TO PDF  ===================================

import pdfkit
pdfkit.from_url(r'https://pypi.org/project/pdfkit/','out2.pdf')
from weasyprint import HTML,CSS

css= CSS(r'bootstrap-5.1.3-dist/css/bootstrap.min.css')
#HTML(string=t).write_pdf('outahere.pdf',stylesheets=[css])
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




























