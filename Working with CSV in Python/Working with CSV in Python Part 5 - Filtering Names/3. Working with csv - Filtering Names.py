# To Do
"""
TO DO: Normalize the names column by replacing all emails with
    corresponding full names so each each record can be idenitied by the
    full name of the learner.
    
    STEPS:
        - define a function to replace emails
        - write a function that applies the cleaning to any 
        number of progress files
    
"""
#============================= PART 2 ========================================
# Clean Names Column
#=============================================================================
# Import Libraries
import pandas as pd

#Load data
progress_df = pd.read_csv('data/progress_data/Analyze Data with Python.csv')
names_df = pd.read_csv('data/names.csv')


def clean_names_column(names_df,progress_df):
    """
    # 1. read in names df
    # 2. read in progress data
    # 3. create a sperate list for names and emails to use in filtering
    # 4. create a dictionary mapping to map email to name
    # 5. join the two dfs
    # 6. return the cleaned data


    Parameters
    ----------
    names_df : TYPE
        DESCRIPTION.
    progress_df : TYPE
        DESCRIPTION.

    Returns
    -------
    pandas dataframe

    """
    
    name_list = [name.strip() for name in names_df.name.values]
    email_list =[email.strip() for email in names_df.email.values]
    
    email_name_map = {email:name for name,email in names_df[['name','email']].values}
    
    # pick out the names that are emails and replace them accordingly
    clean = progress_df[progress_df.name.isin(name_list)]
    to_correct = progress_df[progress_df.name.isin(email_list)]
    
    to_correct['name'] = to_correct['name'].map(email_name_map)
    # update name column with full names
    
    cleaned_df = pd.concat([clean,to_correct])
        
    return cleaned_df
    


df = clean_names_column(names_df =names_df,progress_df=progress_df)


df.to_csv('data/cleaned_data/cleaned.csv')









#============================= PART 3 ========================================
# Filter Names
#=============================================================================
"""
TO DO:
    Filter the progress file so that it contains only learners enrolled in 
    the course
    
    columns: name,started_at,completed_at, percent_complete
    
    1. To filter the data we need a column that gives us a way to
        tell whether someone is enrolled or not.
        
    2. the track column has that info, so we must find a way to add in
        the track info
    
    STEPS:
        
    i. Create a function to add 'track' information
    ii. Add enrollment status based on track information. 
        Use track info to decide if leaner is enrolled in this course
        or not. Create a new column 'enrolled' with Yes/No values for
        each row
    iii. Based on values in the 'enrolled' column, filter out those 
        records with 'No' values
    
   
        
"""
import pandas as pd
import os
import json

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
  
    return "key doesn't exist"
# ********************** HELPER CODE ENDS HERE ************************* 




progress_file = 'data/cleaned_data/Analyze Data with Python.csv'

demo_csv = pd.read_csv(progress_file)
names_df = pd.read_csv('data/names.csv')


def add_track_info(progress_df,names_df):
    """
    Given the progress data, add the track info for each record.

    Parameters
    ----------
    progress_df : pandas df
        DataFrame containing progress data.
    
    names_df : pandas df
        DataFrame containing a names and track info for each record.
        This info is not in the pogress df
    Returns
    -------
    None.

    """
    course_name = os.path.splitext(os.path.basename(progress_file))[0]
    
    
    # add column for track info
    name_track_map = dict(names_df[['name','track']].values)
    progress_df['track'] = progress_df['name'].map(name_track_map)
    
    progress_df['course'] = course_name
    
    return progress_df


def tag_enrollment(course_code,track):
    """
    Determine whethere a leaner in the current progress file is enrolled based
    their track information
    
    Sol: If this course is on the course list for the track 
    enrolled, then this person is enrolled in the course
    """
    track_courses = TRACK_COURSE_MAPPING.get(track,'')
    
    if course_code in track_courses:
        enrolled = 'Yes'
    else:
        enrolled = 'No'
        
    return enrolled



def add_enrollment_info(progress_df,course_name):
    course_code =  course_name_to_code(course_name)
    temp =[]
    for record in progress_df.to_dict(orient = 'records'):
        temp.append(tag_enrollment(track= record['track'], course_code = course_code))
    
    progress_df['enrolled'] = temp
    return progress_df


def filter_names(progress_df):
    """
    Filter the current progress data to include only those enrolled in it

    Parameters
    ----------
    progress_df : pandas df
        progress data.

    Returns
    -------
    progress df

    """
    #Keep only records for those enrolled in course
    return progress_df[progress_df.enrolled == 'Yes']








def process(progress_df):
    """
    Put all the steps together ans execute for a single progress data
    

    Parameters
    ----------
    progress_df : pandas df
        progress data.

    Returns
    -------
    progress df
    
    1. get the course name
    2. add track info
    3. add enrollment info
    4. filter the resulting DataFrame
    """
    course_name = os.path.splitext(os.path.basename(progress_file))[0]
    progress_df = add_track_info(progress_df = demo_csv, names_df = names_df)
    progress_df = add_enrollment_info(progress_df,course_name)
    progress_df = filter_names(progress_df)
    
    return progress_df




progress_file = 'data/cleaned_data/Analyze Data with Python.csv'

demo_csv = pd.read_csv(progress_file)
names_df = pd.read_csv('data/names.csv')

process(demo_csv).to_csv('data/cleaned_data/filtered.csv')







