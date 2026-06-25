from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
load_dotenv()

chat_template = ChatPromptTemplate([
    ('system' , 'you are a helpful {domain} expert.'),
    ('human' , 'explain in simple terms . what is {topic}')
    # SystemMessage(content='you are a helpful {domain} expert.'),
    # HumanMessage(content='explain in simple terms . what is {topic}')

])

prompt = chat_template.invoke({
    'domain':'criket',
    'topic':'dusra'
})

print(prompt)