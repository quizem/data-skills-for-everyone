"""
Write code to extractact structured data from server log file
for onward analysis
    

TO DO
======
    1. Read log file
    2. Parse the data - observe the structure and to extract
    3. Clean data
    4. Analyze as needed **
    
"""
from parse import parse

with open('./data/access_log_Jul95.txt', 'r') as handle:
    data = handle.readlines()
    
#fmt = 'hi {name}, how old is your {animal}'.format(name='Jon', animal='dog')

example = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245'

fmt = '{host} - - [{time}] "{request}" {status} {size}'


# parse all the data

import pandas as pd

parsed_data = map(lambda x: parse(fmt,x).named, data)
df = pd.DataFrame(parsed_data)
















