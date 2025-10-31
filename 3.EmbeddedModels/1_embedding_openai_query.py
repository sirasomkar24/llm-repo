from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32) #dimensions for output context vector size

result= embedding.embed_query("Delhi is the capital of India") #Vector with 32 dimension will be generated with this text
print(result) # this will represent the vector of 32 dimesion with contextual meaning
