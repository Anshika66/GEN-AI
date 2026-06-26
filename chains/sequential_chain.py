from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt1 = PromptTemplate(
    template="generate a detailed report on {topic}",
    input_variables=['topic']
)

model = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()




prompt2 = PromptTemplate(
    template='extract 5 most important features from {text}',
    input_variables=['text']
)



chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic' : 'generative ai' })

print(result)

chain.get_graph().print_ascii()

