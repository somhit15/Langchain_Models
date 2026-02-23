from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Nanbeige/Nanbeige4.1-3B",
    task="text-generation",
    #max_new_tokens=512,
    temperature=0.7,
    #huggingfacehub_api_token=os.getenv("HF_TOKEN"),
)

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("What is the capital of India ?")

print(result.content)