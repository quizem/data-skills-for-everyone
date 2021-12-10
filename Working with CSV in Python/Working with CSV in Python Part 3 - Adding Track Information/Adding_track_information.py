#============================= PART 3 ========================================
# Add track information
#=============================================================================
"""
TO DO:
    Filter the progress file so that it contains only learners enrolled in 
    the course
    
    columns: name,started_at,completed_at, percent_complete
    
    To filter the data we need a column that gives us a way to
    tell whether someone is enrolled or not. The 'track' information
    can help us to decide
        
    1. add 'track' information to the data
    3. use the 'track' info to determine enrolment of each leaner for the 
       course
    
    STEPS:
        
    i. define 'add_track_info()' function
    ii. apply function to the data
    iii. save output to file
    
        
"""
import pandas as pd
import os
import json


# read in progress data
progress_file = 'data/cleaned_data/Analyze Data with Python.csv'
progress_data = pd.read_csv(progress_file)
names_df = pd.read_csv('data/names.csv')


# ********************** HELPER CODE *************************
# Helpers are additional code to perform intermediate steps
# we need them to simply the code for our main task



# ********************** HELPER CODE ENDS HERE ***************

def add_track_info(progress_df, names_df):
    
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


output_df = add_track_info(progress_data, names_df)

output_file = 'data/cleaned_data/edited_file.csv'

output_df.to_csv(output_file)







