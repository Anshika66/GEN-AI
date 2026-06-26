from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

loader = DirectoryLoader(
    path='/Users/apple/Desktop/Artificial Intelligence/GEN AI/document_loader/books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# load takes a lot of time 
# docs = loader.load()

# for document in docs:
#     print(document.metadata)

# lazy_load will take very less amount of time 

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)

