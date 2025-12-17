## HuggingFace models' access through API (access token)
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint # HuggingFaceEndpoint is used when we 
# want to access the API of Huggingface
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
# here, llm is used to access which model is to be used and what is the task that is to be performed

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)
## this python file is throwing the error upon run