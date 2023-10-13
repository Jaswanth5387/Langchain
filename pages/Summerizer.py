import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

st.title('🦜🔗 Summerizer App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    llm=OpenAI(temperature=0.7,openai_api_key=openai_api_key)
    prompt_temp=PromptTemplate.from_template("Please summerize the {content}.")
    chains=LLMChain(llm=llm,prompt=prompt_temp)
    st.info(chains.run(text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)