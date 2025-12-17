from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(template="Generate 5 interesting facts about {topic}", input_variables=['topic'], validate_template=True)

model = ChatOpenAI()

parser = StrOutputParser()

# now, joining all the above three steps through Chain
chain = prompt | model | parser
## the above format is called as 'LCEL = LangChain Expression Language'

result = chain.invoke({'topic': 'Fruits'})
print(result)
chain.get_graph().print_ascii() # pip install grandalf