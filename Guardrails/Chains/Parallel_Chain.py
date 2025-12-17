from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel # used for parallel chain

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(template= 'Generate short and simple notes from the following \n{text}', input_variables= ['text'], validate_template=True)
prompt2 = PromptTemplate(template= 'Generate 5 short question answers from the following text \n {text}', input_variables= ['text'], validate_template= True)
prompt3 = PromptTemplate(template= 'Merge the following notes and quiz into a single document, notes -> {notes} and quizes -> {quiz}', input_variables= ['notes', 'quiz'], validate_template= True)

parser = StrOutputParser()

parallel_chain = RunnableParallel({'notes': prompt1 | model | parser, 'quiz' : prompt2 | model | parser})

merge_chain = prompt3 | model | parser

## making the final chain - parallel_chain connected with merge_chain
chain = parallel_chain | merge_chain

text = """
In Generative AI, prompts can be broadly categorized into three main types: N-shot prompting (including zero-shot, one-shot, and few-shot prompting), Chain-of-thought (CoT) prompting, and Generated knowledge prompting. Additionally, prompt engineering involves various techniques like directive, contextual, and iterative prompting to guide the AI towards desired outputs. 
1. N-shot Prompting:
Zero-shot Prompting:
This approach involves providing the model with a prompt for a task without any examples. The AI relies on its pre-existing knowledge to perform the task. 
One-shot Prompting:
A single example of an input-output pair is provided to the model to guide its response. 
Few-shot Prompting:
The model is given a small number of examples (typically 1 to a few) before being asked to perform a similar task. 
2. Chain-of-thought (CoT) Prompting:
This technique encourages the AI to explain its reasoning step-by-step, leading to more coherent and contextually accurate responses. 
3. Generated Knowledge Prompting:
This involves using AI to generate additional knowledge or context to enhance the prompt and guide the model's response. 
Beyond these core types, prompt engineering involves:
Directive Prompts: Clear instructions are provided to the AI, specifying the desired task and output. 
Contextual Prompts: Relevant background information is included in the prompt to provide the AI with a better understanding of the task. 
Iterative Prompting: The prompt is refined based on the AI's initial output, guiding the model towards the desired outcome. 
Prompt Chaining: Multiple prompts are used sequentially to achieve a complex task. 
Creative Prompts: These encourage the AI to generate innovative and imaginative outputs. 
Reflective Prompts: These prompts encourage the AI to consider its own reasoning and assumptions. 
"""

result = chain.invoke({'text': text})
print(result)
print(chain.get_graph().print_ascii())