from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatOpenAI()

paper_input = st.selectbox("Select Research Paper Name:", ["Attention is all you need", "BERT", "GPT-3"])
style_input = st.selectbox("Select Explanation Style:", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length_input = st.selectbox("Select Explanation Length:", "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (Detailed explanation)")
## these are provided for the users to select from the drop-down based on which the output will come

template = load_prompt('template.json')

# filling the placeholders
prompt = template.invoke({'paper_input': paper_input, 'style_input': style_input, 'length_input': length_input})

if st.button("Suumarize"):
    result = model.invoke(prompt)
    st.write(result.content)