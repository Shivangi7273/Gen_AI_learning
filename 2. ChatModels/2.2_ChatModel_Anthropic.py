## just like OpenAI, Anthropic also provides paid service, and so in order to get the access of the API key
## we have to pay for it

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0, max_tokens_to_sample=10)
result = model.invoke("What is the capital of India?")
print(result)
print(result.content)
