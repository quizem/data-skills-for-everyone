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


Refs:
    https://matplotlib.org/stable/tutorials/colors/colormaps.html
    https://www.textfixer.com/tutorials/common-english-words.txt

"""
#===================== IMPORTS =============================================
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pathlib import Path

#===================== LOAD DATA =============================================

PARENT_FOLDER = os.getcwd()
DATA_FOLDER = Path(r'.\data')



def get_files(file_path=DATA_FOLDER):
    data_files = []
    for root_folder,folders,files in os.walk(DATA_FOLDER):
        
        
        for file in files:
            if file.endswith('.txt'):
                data_files.append(os.path.join(root_folder,file)) 
    
    return data_files

data = []

for file in get_files():
    with open(file,'r',encoding='utf-8',) as filedata:
        data.append(filedata.read())

text = ''.join([ d.split('#')[2] for d in data])            

    

#=================== PREPROCESS DATA =========================================
"""
-remove unwanted character such as punctuationns etc. 
This is done for you by wordcloud package

-if you have specific prior words you don't want to include. 
By default, common English stopwords are removed
https://www.textfixer.com/tutorials/common-english-words.txt
"""



#=================== CONFIGURE WORD CLOUD SETTINGS ===========================
wordcloud_settings = {
'background_color':'black',
'font_path':r".\fonts\RobotoSlab-Bold.ttf",
'include_numbers':False,
'min_word_length':5,
'width':800,
'height':500,
'colormap':'Reds',
'scale':6,
}


#=================== GENERATE WORDCLOUD ======================================

def wordcloud_from_text(text=text,wordcloud_settings=wordcloud_settings):
    """
    

    Parameters
    ----------
    text : str, required
        DESCRIPTION. The text to use for wordcloud.
    wordcloud_settings : dict, optional
        DESCRIPTION. A dict of wordcloud settings.
        The default is wordcloud_settings.

    Returns
    -------
    None.

    """
    cloud = WordCloud(**wordcloud_settings)
    out = cloud.generate(text)
    plt.imshow(out,interpolation="bilinear",cmap='autumn')
    plt.axis('off')
    plt.savefig('wordcloudfromtext.png',dpi=300)
    plt.show()

wordcloud_from_text()


# automate
import argparse
import configparser

def main(source,dest):
            
        #main(args.source,args.output)
        data = []
        for file in get_files():
            with open(file,'r',encoding='utf-8') as datafile:
                data.append(datafile.read())
        text = ''.join([d.split('#')[2] for d in data])
        gencloud(text,out=args.output)



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
            
        main(args.source,args.output)


