from llama_index.llms.openai import OpenAI
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv

load_dotenv()
# print(os.environ["OpenAI_API_Key"])

def main(url:str)-> None:
    document = SimpleWebPageReader(html_to_text=True).load_data(urls = [url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is Generative ai?")

if __name__ == "__main__":
    main(url="https://www.coursera.org/in/articles/what-is-generative-ai")