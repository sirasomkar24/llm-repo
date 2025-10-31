from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI() # Selects the default model

# Keeping the record of the chat history

# Problem with this approach is that as the chat history grows, its difficult for the model to identify which one user's prompt and which one model's output
# so this problem has been resolved in langchain which keeps record in dict which segregate the user's msg from model's prompt

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() in ["exit", "quit"]:
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ",result.content)

print(chat_history)

