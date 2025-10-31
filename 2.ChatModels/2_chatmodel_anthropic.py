from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

# API Key for the Anthropic model is not available in .env file

model = ChatAnthropic(model='claude-sonnet-4-5-20250929')

result = model.invoke('what is the capital of India?')

print(result.content)