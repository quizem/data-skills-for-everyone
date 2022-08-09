# TO DO
"""
- Save the output of a pandas data analysis to disk as text

HOW:
    - generate data as needed
    - format it for saving
    - save to disk
"""
import pandas as pd
from faker import Faker
fake = Faker()

def generate_data(number=5):
    # author
    # title
    # text
    return [{'author':fake.name(), 'title': fake.sentence(), 'text':fake.text(max_nb_chars=100)} for n in range(number)]


generate_data()

df = pd.DataFrame(generate_data(100))

#save to disk

records = df.to_dict(orient = 'record')
records[0]
for i,record in enumerate(records):
    output = "#author {} \n#title {}\n{}".format(record['author'],record['title'],record['text'])
    
    # ensure there is a folder called records in the working directory, or use 
    # another folder of your choice
    
    fname = './records/record' + str(i+1) + '.txt'
    with open(fname,'w',encoding='utf8') as out:
        out.write(output)