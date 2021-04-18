import os
import openai
openai.api_key = os.environ.get('OPENAI_API_KEY')
print(openai.File.list())
openai.File.create(
  file=open("output.jsonl"),
  purpose='classifications'
)
print(openai.File.list())
# openai.File("file-4cL0SASg3TB5BgJB2OzGFBjO").delete()
print(openai.File.list())