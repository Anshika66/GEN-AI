from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough
from pydantic import BaseModel,Field 
from typing import Literal

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'write a joke on the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='explain the following joke - {text}',
    input_variables=['text']
)

joke_generater = RunnableSequence(prompt1 , model , parser)

chain1 = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explaination' : prompt2 | model | parser
})


final_chain = RunnableSequence(joke_generater | chain1)

res = final_chain.invoke({'topic' : 'AI'})

print(res)

