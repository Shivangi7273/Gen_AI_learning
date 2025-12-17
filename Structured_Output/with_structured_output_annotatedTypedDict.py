from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI()

## defining a schema
class review(TypedDict):
    summary: Annotated[str, 'A brief summary of the review']
    sentiment: Annotated[str, 'Whether a sentiment is positive, negative or neutral']
    key_themes: Annotated[list[str], 'Write all the key themes discussed in the review']
    pros: Annotated[Optional[list[str]], 'Write down all the pros inside a list']
    cons: Annotated[Optional[list[str]], 'Write down all the cons inside the list']

structured_model = model.with_structured_output(schema=review)
result = structured_model.invoke("""The hardware feels great but the software feels bloated. There are too many pre-installed apps that can't be removed. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(type(result))
print(result)
print(result['summary'])
print(result['sentiment'])
print(result['pros'])
print(result['cons'])
print(result['key_themes'])
