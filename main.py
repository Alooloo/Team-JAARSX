import os
import openai
from pyexcel_xlsx import get_data;
# from flask import Flask, flash, request, redirect, url_for
# from werkzeug.utils import secure_filename



openai.api_key = os.getenv("OPENAI_API_KEY")
##Getting Input
Array=[]

data = get_data("GPT-3-Hackaton-Dataset-handout.xlsx")
sheetName = 'toConvert'

row = 10
input = data[sheetName][row][2]

print(input)
results = []

response = openai.Completion.create(
    engine="davinci-instruct-beta",
    prompt="Extract the PO  and  Positions from the PROMPT:\n\n###\nPROMPT:\n\nBellungen schließen.\n \nBitte um Schließung der folgenden beiden Bestellungen.\n9705845183\n1003615617\nR/GA MEDIA GROUP INC\n12.09.2020\nBBIP\nIC-BBIPX-BRMOV-YYCM-GM\n1003615617\n 9705884321 4\n9705312321 all\n 9705603654 5\n9705603654 25\nR/GA MEDIA GROUP INC\n30.09.2020\nBBIP\n9705603213\n12\nIC-BBIPX-BRMOV-YYCM-ZV\nVielen Dank.\n\nDATA:\n\nPO: 9705845183\nPositions: alle\n\nPO: 9705884321\nPositions: 4\n\nPO: 9705312321\nPositions: alle\n\nPO: 9705603654\nPositions: 5\n\nPO: 9705603654\nPositions: 25\n\nPO: 9705603213\nPositions: 12\n\n###\nPROMPT:\n\n9703997945, bitte ELK entfernen . \n-----\n9704045358, bitte ELK entfernen \nImportance: High\n \nbitte das Endlieferungkennzeichen für o.a. Bestellung entfernen, damit WE gebucht werden kann.\nVielen Dank.\n\nDATA\n\nPO: 9703997945\nPositions: alle\n\nPO: 9704045358\nPositions: alle\n\n###\nPROMPT:\n\nBitte Bestellung abschließen. bitte schließen Sie folgende Bestellungen ab:\nBZ 9703560965\nBZ9703523062\nBZ \n9703588428, Pos. 1-10\nBZ \n9703635272, Pos. 1-2\nBZ \n9703215352, Pos. 1 + 2\nBZ \n9704663371\n\nDATA:\n\nPO: 9703560965\nPositions: alle\n\nPO: 9703523062\nPositions: alle\n\nPO: 9703588428\nPositions: 1-10\n\nPO: 9703635272\nPositions: 1-2\n\n\nPO: 9703215352\nPositions: 1,2\n\nPO: 9704663371\nPositions: alle\n\n###\n\nPROMPT:\n" + input + "\n\nDATA\n\n",
    temperature=0.5,
    max_tokens=610,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["###"]
)

schleife=True
AnzahlPO=0

for choice in response.choices:
    promtResults=choice.text
while schleife:
    start=promtResults.find("PO: ")
    promtResults=promtResults[start+3:]
    if start==-1:
        schleife=False
    if schleife==True:
        AnzahlPO = AnzahlPO + 1

for choice in response.choices:
    promtResults=choice.text
schleife=True
AnzahlPosition=0
while schleife:
    start=promtResults.find("Positions:")
    promtResults = promtResults[start + 9:]
    if start==-1:
        schleife=False
    if schleife == True:
        AnzahlPosition=AnzahlPosition+1

tmpString=""
if (AnzahlPosition==AnzahlPO):
    for i in AnzahlPosition:
        for choice in response.choices:
            tmpString = response.choices.text
        indexPosition=tmpString.find("Positions:")
        tmpString=tmpString[:indexPosition+10]
        indexPosition = tmpString.find("/n")
        results.append(tmpString[:indexPosition])




for choice in response.choices:
    print(choice.text)

##Classification according to action
response = openai.Classification.create(
    file="file-EMhL3Y86JuZGoeG4Qb0jujRB",
    query=input + "/n/n for Target PO X ",
    search_model="davinci-instruct-beta",
    model="davinci-instruct-beta",
    max_examples=5
)

print(response.label)

print(data[sheetName][row][4])

##POs and Positions.

##Take Pos and classify them according to Type

# for Po in Pos:
#   response = openai.Classification.create(
#     file="file-EMhL3Y86JuZGoeG4Qb0jujRB",
#     query="Endrechnungskennzeichen. Bitte in folgenden Bestellungen das Endrechnungskennzeichen setzen. 9704530974 9704679737  Vielen Dank!",
#     search_model="ada",
#     model="curie",
#     max_examples=5
#   )
##Get Type back as response of queery
#Type=Labels




##Classification according to action
response = openai.Classification.create(
    file="file-EMhL3Y86JuZGoeG4Qb0jujRB",
    query="Endrechnungskennzeichen. Bitte in folgenden Bestellungen das Endrechnungskennzeichen setzen. 9704530974 9704679737  Vielen Dank!",
    search_model="ada",
    model="curie",
    max_examples=5
  )

#action=label


#Put everything together and write them into the excel file G Column






# UPLOAD_FOLDER = '/Users/besitzer/PycharmProjects/Siemens'
# ALLOWED_EXTENSIONS = {'xlsx'}
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER