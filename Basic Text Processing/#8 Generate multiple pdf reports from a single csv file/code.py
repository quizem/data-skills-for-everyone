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


#===================== GENERATE DATA ========================================
# We fake some class data from the normal distribution

class_averages = {
    'math': 65,
    'physics':70,
    'chemistry': 59,
    
    }
number_of_students = 35
sigma = 25

math_grades = np.round(np.random.normal(loc = class_averages['math'],
                               scale = sigma,
                               size = number_of_students),1)

physics_grades = np.round(np.random.normal(loc = class_averages['physics'],
                               scale = sigma,
                               size = number_of_students),1)

chem_grades = np.round(np.random.normal(loc = class_averages['chemistry'],
                               scale = sigma,
                               size = number_of_students),1)

df = pd.DataFrame(zip(math_grades,physics_grades,chem_grades),
                  columns=['math','physics','chemistry'])



#===================== 1. LOAD DATA ==========================================
DATA_FOLDER = Path(r".\data")


def get_files(file_path = DATA_FOLDER):
    data_files = []
    
    for root_folder,folders,files in os.walk(file_path):
        for file in files:
            if file.endswith('.txt'):
                data_files.append(os.path.join(root_folder,file))
    return data_files


def load_data(data_source):
    data = []
    
    for file in get_files(data_source):
        with open(file,'r',encoding='utf-8') as datafile:
            data.append(datafile.read())
    
    return ''.join([d.split('#')[2] for d in data])

text = load_data(data_source = DATA_FOLDER)

#=================== 3. PREPROCESS DATA ======================================


#=================== 4. CONFIGURE WORD CLOUD SETTINGS ========================



#=================== 5. GENERATE WORDCLOUD ===================================


# Automate everything we have done


def automate(source,destination):
    text = load_data(source)
    gencloud(text =text, destination = destination)
    

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




























