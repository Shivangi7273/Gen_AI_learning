from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import os
from dotenv import load_dotenv

load_dotenv()

# Step 1 -
# Your source documents -
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily"),
    Document(page_content='Chroma is a vector data base optimized for LLM based search'),
    Document(page_content="Embeddings convert text into high dimensional vectors"),
    Document(page_content="OpenAI provides powerful embedding models"),
]

# Step 2 -
# Initializing the embedding model
embedding = OpenAIEmbeddings()

# Step 3 -
# Creating Chroma vector store in a memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    collection_name = 'my_collection'
)

# Step 4 -
# Converting vectorstore into retriever
retriever = vectorstore.as_retriever(search_kwargs = {'k':2})

query = 'What is Chroma used for?'
result = retriever.invoke(query)

for i, doc in enumerate(result):
    print(f"-----------Result {i+1} ----")
    print(f"-------Content----- {doc.page_content}")