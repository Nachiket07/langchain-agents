import os
from dotenv import load_dotenv
#pip install python-dotenv
from langchain.chat_models import init_chat_model
#pip install -U langchain-google-genai

load_dotenv("../local.env")
f = "Hello world!"
print(f)
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

response = model.invoke("Why do parrots talk?") 
print(response)
#https://docs.langchain.com/oss/python/langchain/models#google-gemini