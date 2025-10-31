from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI() # Selects the default model
# This is the simplest chatbot which can not keep the record of the previous (no context) chat reference, its a stateless chat

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    result = model.invoke(user_input)
    print("AI: ",result.content)

