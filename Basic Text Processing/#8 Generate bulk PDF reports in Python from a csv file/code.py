"""
Generate pdf reports in bulk using a single csv file

TO DO
======
We are going generate a PDF report for each record in the CSV file using a 
predefined HTML template

    0. Data generation [Optional]
    1. Load and inspect data
    2. Preprocessing - generate grade letters
    3. Quick review python string formatting
    4. A simple template using Python string formatting
     - [Optional] Use Jinja2 template engine
    4. Generate pdf using weasyprint

"""
#===================== IMPORTS ===============================================
import os
from pathlib import Path
import numpy as np
import pandas as pd
from weasyprint import HTML,CSS
from helpers import get_grade_letter, calculate_gpa, total_gpa

#===================== 1. LOAD DATA ==========================================
data_file = Path('./data/records.csv')
df = pd.read_csv(data_file)

#===================== 2. PROCESS DATA =======================================
records = df.to_dict(orient = 'records')
record = records[0]

report = {}

report['student'] = record['name']
report['math_score'] = record['math']
report['math_grade'] = get_grade_letter(record['math'])
report['math_gpa'] = calculate_gpa(record['math'])

report['physics_score'] = record['physics']
report['physics_grade'] = get_grade_letter(record['physics'])
report['physics_gpa'] = calculate_gpa(record['physics'])

report['chemistry_score'] = record['chemistry']
report['chemistry_grade'] = get_grade_letter(record['chemistry'])
report['chemistry_gpa'] = calculate_gpa(record['chemistry'])

report['total_gpa'] = total_gpa(record['math'],
                                record['physics'],
                                record['chemistry']
    
    )

#=================== 3. A SIMPLE TEMPLATE ====================================

template = """
==================== REPORT CARD ======================
Subject |        Score      | Grade      | GPA
-------------------------------------------------------
                    {student}
Math        {math_score:^7} {math_grade:^7} {math_gpa:^7}
Physics     {physics_score:^7} {physics_grade:^7} {physics_gpa:^7}
Chemistry   {chemistry_score:^7} {chemistry_grade:^7} {chemistry_gpa:^7}
Total GPA   {total_gpa}


"""

output = template.format(**report)



#=================== 4. A BETTER TEMPLATE USING WEASYPRINT  ==================
with open('template2.html','r') as file:
    html_template = file.read()
    
css = CSS('bootstrap-5.1.3-dist/css/bootstrap.min.css')


records = df.to_dict(orient = 'records')

for record in records:

    report = {}
    
    report['student'] = record['name']
    report['math_score'] = record['math']
    report['math_grade'] = get_grade_letter(record['math'])
    report['math_gpa'] = calculate_gpa(record['math'])
    
    report['physics_score'] = record['physics']
    report['physics_grade'] = get_grade_letter(record['physics'])
    report['physics_gpa'] = calculate_gpa(record['physics'])
    
    report['chemistry_score'] = record['chemistry']
    report['chemistry_grade'] = get_grade_letter(record['chemistry'])
    report['chemistry_gpa'] = calculate_gpa(record['chemistry'])
    
    report['total_gpa'] = total_gpa(record['math'],
                                    record['physics'],
                                    record['chemistry']
        
        )

    html = html_template.format(**report)
    
    # Create a folder called `output` in the working directory for the next line to work 
    HTML(string = html).write_pdf('./output/{}.pdf'.format(report['student']), stylesheets=[css])






















#=================== 5. SAVE TO PDF  =========================================
