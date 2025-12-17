# pip install langchain chromadb faiss-cpu openai tiktoken langchain_openailangchain-community wikipedia
## -> to be installed in the terminal

from langchain_community.retrievers import WikipediaRetriever

# initializing the retriever
retriever = WikipediaRetriever(top_k_results=2, lang='en') # top_k_results = no of documents that we want

# define your query
query = "the geopolitical history of India and Pakistan from the perspective of a Chinese"

# get relevant wikipedia documents
docs = retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f"\n Result {i+1} ----")
    print(f"Content - {doc.page_content}")