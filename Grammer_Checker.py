import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title('🦜🔗 Grammer checker App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# def generate_response(input_text):
#     llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
#     st.info(llm(input_text))

# with st.form('my_form'):
#     text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
#     submitted = st.form_submit_button('Submit')
#     if not openai_api_key.startswith('sk-'):
#         st.warning('Please enter your OpenAI API key!', icon='⚠')
#     if submitted and openai_api_key.startswith('sk-'):
#         generate_response(text)

def response(text):
    llm=OpenAI(temperature=0.7,openai_api_key=openai_api_key)
    prompt_temp=PromptTemplate.from_template("Please correct the sentence if there is any mistake in the sentence {content}.")
    chains=LLMChain(llm=llm,prompt=prompt_temp)
    st.info(chains.run(text))
    
with st.form('my_form'):
    text=st.text_area('enter text:','What is the thre ke pieces of advice for learning how to code?')
    submitted=st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')  
    if submitted and openai_api_key.startswith('sk-'):
        response(text)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            

