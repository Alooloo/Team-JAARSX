import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

response = openai.Classification.create(
    file="file-EMhL3Y86JuZGoeG4Qb0jujRB",
    query="Endrechnungskennzeichen. Bitte in folgenden Bestellungen das Endrechnungskennzeichen setzen. 9704530974 9704679737  Vielen Dank!",
    search_model="ada",
    model="curie",
    max_examples=5
)
print(response.label)