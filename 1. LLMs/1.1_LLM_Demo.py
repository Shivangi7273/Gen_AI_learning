from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() ## this helps in loading API key present in .env file

llm = OpenAI(model='gpt-3.5-turbo-instruct')
result = llm.invoke("what is the capital of India?") ## this 'invoke' method is very important in LangChain
print(result)