from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv

load_dotenv()

model = ChatNVIDIA(model="z-ai/glm4.7")

result = model.invoke("What is the capital of India ?")

print(result)