from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough , RunnableLambda , RunnableBranch
from pydantic import BaseModel,Field 
from typing import Literal

load_dotenv()

parser = StrOutputParser()

model = ChatGroq(model="llama-3.3-70b-versatile")

def word_count(text):
    return len(text.split())


prompt1 = PromptTemplate(
    template = 'generate a detailed report on the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='summarize the following text \n {text}',
    input_variable=['text']
)

report_gen = RunnableSequence(prompt1 , model , parser)

branch = RunnableBranch(
    (lambda x : (len(x.split()))>500  , RunnableSequence(prompt2 , model , parser)),
    RunnablePassthrough()
    
)

final_chain = RunnableSequence(report_gen , branch)

res = final_chain.invoke({'topic' : 'russia vs china '})

print(res)
