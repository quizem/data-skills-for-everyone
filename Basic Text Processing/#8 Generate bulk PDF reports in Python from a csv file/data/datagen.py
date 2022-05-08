# -*- coding: utf-8 -*-
"""
TO DO:
    1. Generate data
    
    Refs:
        https://en.wikipedia.org/wiki/Academic_grading_in_the_United_States#Rank-based_grading
"""

#===================== GENERATE DATA [OPTIONAL] ========================================
# We fake some class data from the normal distribution
import pandas as pd
from faker import Faker
import numpy as np
from pathlib import Path

# class averaages to help ggenerate data from normal distribution
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
