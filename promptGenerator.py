import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

email=""

response = openai.Classification.create(
  engine="ada",
  prompt="The following is a list of companies and the categories they fall into\n\nFacebook: Social media, Technology\nLinkedIn: Social media, Technology, Enterprise, Careers\nUber: Transportation, Technology, Marketplace\nUnilever: Conglomerate, Consumer Goods\nMcdonalds: Food, Fast Food, Logistics, Restaurants\nFedEx:",
  temperature=0,
  max_tokens=6,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)
for choice in response.choices:
  print(choice.text)