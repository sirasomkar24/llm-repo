from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

st.header("Research Tool")

model = ChatOpenAI(model='gpt-4',temperature=0)

# user_input = st.text_input("Enter your prompt") # Example of static prompt
paper_input = st.selectbox("Select Research paper name",["Attention is all you need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language models are few shot learners", "Diffusion models Best GANs on image synthesis"],placeholder="Select from dropdown",index=None)

style_input = st.selectbox("Select Explaination style",["Beginner-Friendly","Technical","Code-oriented","Mathematical"],placeholder="Select from dropdown",index=None)

lenght_input= st.selectbox("Select Explaination Length",["Short (1-2 paragraph)", "Medium(3-5 paragraph)", "Long(Detailed Explaination)"],placeholder="Select from dropdown",index=None)

template = load_prompt('./4.LangchainPrompts/prompt_template.json')



if st.button('Summarize'):
    chain = template | model
    result = chain.invoke(
        {
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': lenght_input
    }
    ) 
    st.write(result.content)