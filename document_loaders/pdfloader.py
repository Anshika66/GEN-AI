from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

loader = PyPDFLoader('/Users/apple/Desktop/Artificial Intelligence/GEN AI/document_loader/dl-curriculum.pdf' )

pdfs = loader.load()

print(len(pdfs))
print(pdfs[0].page_content)
print("\n\n")
print(pdfs[0].metadata)

prompt1 = PromptTemplate(
    template = 'Conclude the content of each page of the {text}',
    input_variables=['text']
)

chain = prompt1 | model | parser

res = chain.invoke({'text' :pdfs})

print(res)
