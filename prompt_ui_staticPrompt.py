from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatOpenAI()

st.header("Research tool")
user_input = st.text_input('Enter your prompt')

if st.button('Summarize'):
    st.text('Some random text')
    result = model.invoke(user_input)
    st.write(result.content)