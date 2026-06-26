from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough , RunnableLambda
from pydantic import BaseModel,Field 
from typing import Literal

load_dotenv()

parser = StrOutputParser()

model = ChatGroq(model="llama-3.3-70b-versatile")

def word_count(text):
    return len(text.split())




prompt1 = PromptTemplate(
    template='generate a funny joke on this {topic}',
    input_variables=['topic']
)


chain = RunnableSequence(prompt1 | model | parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'Word_count': RunnableLambda(word_count)
})

final_chain = chain | parallel_chain

res = final_chain.invoke({'topic' : 'eyes'})

print(res)
