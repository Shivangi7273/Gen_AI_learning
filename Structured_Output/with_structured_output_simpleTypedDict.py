from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

## creating the schema - the type of data format for which the output should be delivered
## defining the schema -

## this is Simple TypedDict
class review(TypedDict):
    summary : str
    sentiment: str

structured_model = model.with_structured_output(schema=review)
result = structured_model.invoke("""The hardware feels great but the software feels bloated. There are too many pre-installed apps that can't be removed. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)
print(type(result)) ## here, the type is dictionary
print(result['summary'])
print(result['sentiment'])
