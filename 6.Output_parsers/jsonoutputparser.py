from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",    
    task= "text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

parser= JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of the fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}

)


# Binding into the chain
chain = template | model | parser

result = chain.invoke({})  # since the input variables defined in the template are empty list, chain.invoke expects an input, so put here empty dict

print(result)