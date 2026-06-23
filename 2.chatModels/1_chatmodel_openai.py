from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


chatmodel = ChatOpenAI(model='gpt-4',terperature=0,max_completion_tokens=10)
result = chatmodel.invoke("what is the capital of India?")

print(result.content)

