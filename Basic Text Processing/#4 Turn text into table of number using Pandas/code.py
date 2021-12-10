# To Do
"""
- turn a collection of text into a table of numbers

HOW:
        
    # 1. read in the collection of data
    # 2. do some preprocessing
    # 3. perform some calculations
    
    - using Python loops and string manipulation
    - using Pandas DataFrame
"""
# 1. read in the collection of data
from faker import Faker
fake = Faker()

def generate_data(number=10):
    # title
    # text
    return [{'title':fake.sentence(),'text':fake.text(max_nb_chars=1000)} for n in range(number)]


data = generate_data(1000)

# doing some calculation
# 3. perform some calculations

import pandas as pd
df = pd.DataFrame(data)

# create new
df = df.assign(n_words = lambda x: x.text.apply(lambda y: len(y.split()) ))  
df = df.assign(n_chars = lambda x: x.text.apply(lambda y: len(y)))     

#df[col].apply

df = pd.DataFrame(data)
df['n_words'] = df['text'].apply(lambda x: len(x.split()))
df['n_chars'] = df['text'].apply(lambda x: len(x))

df





