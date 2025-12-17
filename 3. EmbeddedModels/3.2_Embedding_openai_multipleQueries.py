from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
documents = [
    "Delhi is the capital of India",
    "Delhi is also a metropolitan city"
]

multiple_embeddings = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=2)
result = multiple_embeddings.embed_documents(documents)
print(str(result))