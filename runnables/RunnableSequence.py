from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableSequence
from pydantic import BaseModel,Field 
from typing import Literal

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'write a joke on the {topic}',
    input_variable=['topic']
)

prompt2 = PromptTemplate(
    template='explain the following joke - {text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt1 , model , parser , prompt2 , model , parser)

result = chain.invoke({'topic' , 'Ai'})

print(result)

chain.get_graph().print_ascii()