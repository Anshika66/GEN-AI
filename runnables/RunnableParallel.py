from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel
from pydantic import BaseModel,Field 
from typing import Literal

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template = 'generate a tweet on this {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate a linkedin post on this {topic}',
    input_variables=['topic']
)

chain = RunnableParallel(
    {
        'tweet' : prompt1 | model | parser,
        'post' : prompt2 | model | parser
    }
)


res = chain.invoke({'topic' : 'generative ai'})
print("tweet : \n" ,res['tweet'])
print("\n")
print("post : \n" ,res['post'])


