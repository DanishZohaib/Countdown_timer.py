# I am creating my own chatboat using OpenAI
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4")

userInput = input("Enter what you want to ask: ")
response = model.invoke(userInput)

print(f"GPT RESPONSE: {response.content}") 