"""
Write code to read the text file and print out the 5 top-selling 
key products, in descending order of sales. 
The expected output for the given file should look as follows:
    
1. Phone 
2. Tablet 
3. RGB Coffee Mug 
4. PC 
5. Webcam 

==>>> NOTE:
For the purpose of this example, assume all items sold will be in 
thousands or milions.

TO DO
======
    1. Read text file
    2. Parse the data - observe the structure and to extract
    3. Clean data
    4. Sort
    5. Write output

"""
#  1. Read text file

with open('./data/summary.txt','r') as file_handle:
    raw_data = file_handle.readlines()
    
key_products = raw_data[10:19]

#2. Parse the data - observe the structure and to extract
# data must look like this [('keyboard',3),('Note',11)]
#[('keyboard',3),('Note',11)]

key_products = [row.strip().replace(')','').split('(') for row in key_products]

key_products = [[row[0]] + row[1].split(" ")[:2] for row in key_products]

# sort data: sorted



result = []
for row in key_products:
    if row[2] == 'thousand':
        result.append((row[0],float(row[1])*1000))
    else:
        result.append((row[0],float(row[1])*1000000))
        

# sorting
top_five = sorted(result,key = lambda x: x[1], reverse=True)[0:5]



# printing out in required format

for i,item in enumerate(top_five):
    print("{num}. {item_name}".format(num=i+1, item_name=item[0]))




















