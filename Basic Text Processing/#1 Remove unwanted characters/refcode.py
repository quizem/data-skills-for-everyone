# To DO
"""
- Obtain some text- news article 
- replace punctuations
- replace some words of interest

HOW:
    - read in text data
    - use python string library to generate punctuations
    - write some functions to achieve our goals
"""

# 1 Remove punctuations
# 2 Remove list of words
# 3 REmove whitespaces from start or end
# 4 Remove white spaces from both ends

#1 
with open('article.txt','r',encoding='utf8') as inf:
    article = inf.readlines()
    
import string
punctuations =  string.punctuation

# method 1 : too slow
cleaned_article =[]

for line in article:
    temp =line
    for p in punctuations:
        temp = temp.replace(p,'')
    cleaned_article.append(temp)
    
# method 2: Better
x= ''
y =''
z = string.punctuation
#trans_table = sample.maketrans(x,y,z)

for line in article:
    trans_table = line.maketrans(x,y,z)
    cleaned_article.append(line.translate(trans_table))
    

# Remove list of words
import re
words_to_replace = ['and','the','that']


cleaned_article = ''.join(cleaned_article)
words = cleaned_article.split()
len(words)


words = ' '.join(words)
