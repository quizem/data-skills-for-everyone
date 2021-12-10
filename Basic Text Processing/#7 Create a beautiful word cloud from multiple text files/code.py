"""
TO DO
======

1. read data
2. combine files into a single one
3. Optional preprocessing
   Notes:
       - default preprocessing will be applied 
       - e.g. stopword removal, plural normalization
       - you can add additional steps to remove more words you want
    
4. configure wordcloud settings
5. explore different options for word cloud creation
   - create word cloud from raw text
   - generate from frequecies (this could be another video)
   
6. automate wordcloud creation

"""
#===================== IMPORTS ===============================================
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pathlib import Path



#===================== 1. LOAD DATA ==========================================
DATA_FOLDER = Path(r".\data")


def get_files(file_path = DATA_FOLDER):
    data_files = []
    
    for root_folder,folders,files in os.walk(file_path):
        for file in files:
            if file.endswith('.txt'):
                data_files.append(os.path.join(root_folder,file))
    return data_files


def load_data(data_source):
    data = []
    
    for file in get_files(data_source):
        with open(file,'r',encoding='utf-8') as datafile:
            data.append(datafile.read())
    
    return ''.join([d.split('#')[2] for d in data])

text = load_data(data_source = DATA_FOLDER)

#=================== 3. PREPROCESS DATA ======================================
"""
-remove unwanted character such as punctuationns etc. 
This is done for you by wordcloud package

-if you have specific prior words you don't want to include. 
By default, common English stopwords are removed
https://www.textfixer.com/tutorials/common-english-words.txt
"""



#=================== 4. CONFIGURE WORD CLOUD SETTINGS ========================
wordcloud_settings = {
'background_color':'black',
'font_path':r".\fonts\RobotoSlab-Bold.ttf",
'include_numbers':False,
'min_word_length':0,
'width':800,
'height':500,
'colormap':'Reds',
'scale':6,
}

#Oranges,Reds

#=================== 5. GENERATE WORDCLOUD ===================================
def gencloud(text,settings = wordcloud_settings,destination=None):
    
    cloud = WordCloud(**settings)
    output = cloud.generate(text=text)
    plt.imshow(output,interpolation='bilinear')
    plt.axis('off')
    
    if destination:
        output_file = os.path.join(destination, 'wordcloud.png')
        plt.savefig(output_file,dpi=300)
    else:
        plt.savefig('wordcloud.png',dpi=300)


gencloud(text,settings = wordcloud_settings,destination=None)


# Automate everything we have done


def automate(source,destination):
    text = load_data(source)
    gencloud(text =text, destination = destination)
    

import argparse
import configparser
if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('-s','--source',type=str,help='source folder',default=r'.\data')
        parser.add_argument('-o','--output',type=str,help='output folder',default=r'.\output')
        
        parser.add_argument('--config', '-c', type=argparse.FileType('r'),help='config file')
        args = parser.parse_args()
        
        if args.config:
            config = configparser.ConfigParser()
            config.read_file(args.config)
            args.source = config['ARGUMENTS']['source_folder']
            args.output = config['ARGUMENTS']['output_folder']
            
        automate(args.source,args.output)




























