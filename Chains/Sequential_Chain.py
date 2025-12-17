from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt1 = PromptTemplate(
    template= "Generate a detailed report of {topic}",
    input_variables= ['topic'],
    validate_template=True
)

prompt2 = PromptTemplate(template= "Generate a 5 pointer summary from the following text \n {text}", input_variables= ['text'], validate_template=True)

model = ChatOpenAI()
parser = StrOutputParser()

## designing a chain
chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'potato'})
print(result)
print(chain.get_graph().print_ascii())
