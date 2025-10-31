from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents = [
"Virat Kohli became the fastest player to reach 8,000 runs in One Day Internationals.",
"India won its first Cricket World Cup in 1983 under the captaincy of Kapil Dev.",
"Sachin Tendulkar is widely regarded as one of the greatest batsmen in the history of cricket.",
"The Indian Premier League (IPL) has revolutionized the way cricket is played and watched in India.",
"Mahendra Singh Dhoni led India to victory in the 2007 T20 World Cup and the 2011 ODI World Cup."
]

user_query = 'tell me about dhoni'

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(user_query)

scores = cosine_similarity([query_embedding],doc_embedding)[0] # Both vectors should be 2D

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(user_query)
print(documents[index])
print("similarity score: ",score)
