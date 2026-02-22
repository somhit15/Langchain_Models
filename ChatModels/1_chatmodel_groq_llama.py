from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

messages = "What is the capital of Jharkhand?"

result = model.invoke(messages)

print(result.content)