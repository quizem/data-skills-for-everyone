# To Do
"""
- Read in a large collection of text files from your computer

HOW:
    - import  os module
    - read in the collection of data using os module
"""

import os
os.getcwd()

data_folder = os.path.join(os.getcwd(),'articles')

# os.walk

#len(list(os.walk(data_folder))[0])

data =[]
for root, folders, files in os.walk(data_folder):
    for file in files:
        path = os.path.join(root,file)
        with open(path) as inf:
            data.append(inf.read())