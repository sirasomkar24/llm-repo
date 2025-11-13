from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model='gpt-5')

# First Prompt --> Detailed report
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)

# Second Prompt --> Summarization
template2 = PromptTemplate(
    template="write a 5 lines of summary on the following text \n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({'topic': 'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result2 = model.invoke(prompt2)

print(result2.content)