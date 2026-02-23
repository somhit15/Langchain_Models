from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv

load_dotenv()

model = ChatNVIDIA(model="z-ai/glm4.7",
                   api_key="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")

result = model.invoke("What is the capital of Jharkhand?")

print(result)