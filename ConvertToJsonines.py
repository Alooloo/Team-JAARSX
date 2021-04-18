from pyexcel_xlsx import get_data;
import time;
import json;
import os
import openai

data = get_data("GPT-3-Hackaton-Dataset-handout.xlsx")
sheetName = 'toConvert'

data_list = []
#len(data[sheetName]
# Iterate through each row and append in above list

for i in range(1, 201):
    tmp=data[sheetName][i][3]
    print(tmp)
    string="Open"
    label=""
    if (tmp.find(string.lower())!=-1):
        label="Open"
    else:
        label="Close"
    data_list.append({
        'text' : data[sheetName][i][2],
        'label' : label,
        'meta data': "Row: "+str(i)+" ID: "+data[sheetName][i][0]
    })
for data in data_list:
    print(data)
#data_list = {'intents': data_list} # Converting to required object
j = json.dumps(data_list)
# Write to file
with open('OutputinJason.json', 'w') as f:
    f.write(j)
with open('output.jsonl', 'w') as outfile:
    for entry in data_list:
        json.dump(entry, outfile)
        outfile.write('\n')

