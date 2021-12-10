#============================= PART 4 ========================================
# Add enrollment information
#=============================================================================
"""
DONE:
    - define 'add_track_info()' function

TO DO:
    Filter the progress file so that it contains only learners enrolled in 
    the course
    
    columns: 
        - name,
        - started_at,
        - completed_at, 
        - percent_complete, 
        - track,
        - course
    
    Given the track information and the course name, we need to determine
    whether a person is enrolled in a course or not
        
    1. add 'enrolment' information to the data
    2. use the 'enrolment' info to filter the records
    
    STEPS:
        
    i. define 'add_enrolment_info()' function
        - define intermediate helper function tag_enrolment()
    ii. apply function to the data
    iii. save output to file
        
"""
#
import pandas as pd
import os
import json

# read in progress data
progress_file = 'data/cleaned_data/edited_file.csv'
progress_data = pd.read_csv(progress_file)
names_df = pd.read_csv('data/names.csv')

# read in track information
TRACK_COURSE_MAPPING = None

with open('data/track_course_mapping.json') as filehandle:
    TRACK_COURSE_MAPPING = json.load(filehandle)


# ********************** HELPER CODE *************************
# Helpers are additional code to perform intermediate steps
# we need them to simply the code for our main task
def course_name_to_code(course_name):
    """
    Returns the course code given a course name

    Parameters
    ----------
    course_name : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    for track in TRACK_COURSE_MAPPING:
        for key, value in TRACK_COURSE_MAPPING[track].items(): 
         if course_name.strip() == value: 
             return key
         
    return "Sorry, course not found"


def tag_enrollment(course_code,track):
    """
 
    Given a specialization track and a course code, 
    determine whether this course is required for learners in this track.
    
    If a course is on the course list for a track, this course is mandatory
    for all leaners in the track.
   

    Parameters
    ----------
    course_code : str
        course code to be tested
    track : str
        specialization track for a learner

    Returns
    -------
    enrolled : str
        Yes/No text indicating whether a learner is enrolled

    """
    track_courses = TRACK_COURSE_MAPPING.get(track,'')
    
    if course_code in track_courses:
        enrolled = 'Yes'
    else:
        enrolled = 'No'
    return enrolled


# ********************** HELPER CODE ENDS HERE ************************* 

def add_enrolment_info(progress_df, course_name):
    """
    Given a progress data and the course name for this data,
    creates a new column, 'enrolled' with Yes/No value for each record

    Parameters
    ----------
    progress_df : pandas DataFrame
        progress data
    course_name : str
        course name for this progress data.

    Returns
    -------
    progress_df : padas DataFrame
        progress data with 'enrolled' column

    """
    course_code =  course_name_to_code(course_name)
    temp =[]
    for record in progress_df.to_dict(orient = 'records'):
        temp.append(tag_enrollment(track= record['track'], course_code = course_code))
    
    progress_df['enrolled'] = temp
    return progress_df


output_df = add_enrolment_info(progress_data,'Analyze Data with Python')
output_df.to_csv('data/cleaned_data/analyze_data_with_python_edited.csv')
