from langchain_openai import ChatOpenAI
## here, we are not importing 'OpenAI' as in LLM, but we are importing 'ChatOpenAI' because we will be working
## on Chat models and not on LLM models [LLM's OpenAI inherits from class 'BaseLLM' and Chat Models's Open AI
## inherits from 'BaseChatModel']

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4', temperature=0, max_completion_tokens=5)
result = model.invoke("What is the capital of India?")
result_2 = model.invoke("Suggest me 5 Indian freedom fighter names")
result_3 = model.invoke("Tell me a story of cricket")
print(result) ## gives all the details along with the answer asked above
print(result.content) ## gives only the answer of the asked question
print(result_2.content)
print(result_3.content)
