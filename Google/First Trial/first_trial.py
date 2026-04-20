import os

from dotenv import load_dotenv
# pip install python-dotenv
from langchain.chat_models import init_chat_model

# pip install -U langchain-google-genai

env_path = os.path.join(os.path.dirname(__file__), "../../secrets/local.env")
load_dotenv(env_path)

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

response = model.invoke("Why do parrots talk?")
print(response)
# https://docs.langchain.com/oss/python/langchain/models#google-gemini
