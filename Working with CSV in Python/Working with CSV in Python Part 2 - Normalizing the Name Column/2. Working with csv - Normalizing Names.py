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











