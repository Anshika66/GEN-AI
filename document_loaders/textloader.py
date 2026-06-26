from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


model = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()



loader = TextLoader('/Users/apple/Desktop/Artificial Intelligence/GEN AI/document_loader/cricket.txt' , encoding='utf-8')

docs = loader.load()

print(docs)

print(len(docs))

print(docs[0].page_content)
print("\n\n")
print(docs[0].metadata)


prompt1 = PromptTemplate(
    template='summarize the given {text}',
    input_variables=['text']
)


chain = prompt1 | model | parser 

res = chain.invoke({'text' : docs[0].page_content})

print(res)

chain.get_graph().print_ascii()