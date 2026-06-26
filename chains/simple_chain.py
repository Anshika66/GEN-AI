from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

prompt = PromptTemplate(
    template="generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

model = ChatGroq(model="llama-3.3-70b-versatile")


parser = StrOutputParser()

chain = prompt | model | parser 

result = chain.invoke({'topic' : "rice"})

print(result)

#to visulaize the chain 
chain.get_graph().print_ascii()
