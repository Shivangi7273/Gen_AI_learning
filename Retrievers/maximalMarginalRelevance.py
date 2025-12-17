from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

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
embedding = OpenAIEmbeddings()

# Step 3 -
vectorstore = FAISS.from_documents(documents=documents, embedding=embedding, 
                                   collection_name = 'my_collection')

# Step 4 -
retriever = vectorstore.as_retriever(search_type= 'mmr', 
                                     search_kwargs ={'k':4, 'lambda_mult':1},
                                     )
## lambda_mult = relevance diversity balance -> its value ranges from 0 to 1
## if the value of 'lambda_mult' is kept as 1 then the results will be similar just like the normal 
## retriever that gives semantic search similar, but if the value is 0 then it will completely behave 
## like MMR and the result will be diverse (different).

query = "What is LangChain?"

result = retriever.invoke(query)

for i, doc in enumerate(result):
    print(f"-----\n {i+1}-----")
    print(f"-----Content{doc.page_content} ---")