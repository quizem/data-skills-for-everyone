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


data = generate_data(10)

# 3. perform some calculations
calculations = []
for d in data:
    # n_words
    # n_chars
    # title_len
    n_words = len(d['text'].split())
    n_chars = len(d['text'])
    title_len = len(d['title'].split())
    calculations.append({'n_words':n_words,'n_chars':n_chars,'title_len':title_len})
    

# datafram
import pandas as pd
df = pd.DataFrame(calculations)
df.to_csv('calculations.csv')
