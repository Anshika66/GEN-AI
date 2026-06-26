from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableParallel , RunnableBranch, RunnableLambda
from pydantic import BaseModel,Field 
from typing import Literal

load_dotenv()

model1 = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

class FeedBack(BaseModel):

    sentiment : Literal['positive' , 'negative'] = Field(description='give the sentiment of the feedback')


parser2 = PydanticOutputParser(pydantic_object=FeedBack)
prompt1 = PromptTemplate(
    template = 'classify the sentiment of the following feedback text into positive or negative \n {feedback}\n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model1 | parser2

result = classifier_chain.invoke({'feedback':'this is a wonderful car' }).sentiment

prompt2 = PromptTemplate(
    template = 'write an appropriate response to this positive feedback\n{feedback}',
    input_variables=['feedback']
)


prompt3 = PromptTemplate(
    template = 'write an appropriate response to this negative feedback\n{feedback}',
    input_variables=['feedback']
)


branched_chain = RunnableBranch(
    #(condition , chain)
    (lambda x : x.sentiment == 'positive' , prompt2|model1|parser),
    (lambda x : x.sentiment == 'negative' , prompt3 | model1 | parser),
    RunnableLambda(lambda x :"could not find sentiment")
)

chain = classifier_chain | branched_chain


result1 = chain.invoke({'feedback' : 'this is a wonderful saari'})

print(result1)

chain.get_graph().print_ascii()
