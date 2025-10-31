from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('system','you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# Load chat history
with open('4.LangchainPrompts/chat_history.txt') as f:
    chat_history.extend(f.readlines())

# create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query':'where is my refund'})

print(prompt)