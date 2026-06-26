from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatGroq(model="llama-3.3-70b-versatile")

model2 = ChatGroq(model="llama-3.3-70b-versatile")



prompt1 = PromptTemplate(
    template='generate short and simple notes from the following text\n {text}',
    input_variables=['text']
)



prompt2 = PromptTemplate(
    template='generate 5 short question answers from the following text\n {text}',
    input_variables=['text']
)



prompt3 = PromptTemplate(
    template='merge the provided notes and quiz into a single document\n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes' , 'quiz']
)

parser = StrOutputParser()


parallel_chain = RunnableParallel(
    {
        'notes' : prompt1 | model1 | parser,
        'quiz' : prompt2 | model2 | parser
    }
)

merege_chain = prompt3 | model1 | parser

chain = parallel_chain | merege_chain

text = """
Support Vector Machine (SVM) is a supervised machine learning algorithm used mainly for classification and 
sometimes regression tasks. Its goal is to find the optimal decision boundary, called a hyperplane, that separates 
different classes with the maximum margin, which helps improve the model's ability to generalize to new data. 
The data points closest to the hyperplane are known as support vectors, and they play a crucial role in determining 
the position of the boundary. For data that is not linearly separable, SVM uses the kernel trick (such as Linear, 
Polynomial, or RBF kernels) to transform the data into a higher-dimensional space where separation becomes possible. 
Important parameters include C, which controls the trade-off between maximizing the margin and minimizing classification
errors, and Gamma, which determines how much influence individual training points have on the decision boundary. 
SVM is widely used in applications such as image recognition, spam detection, text classification, and medical diagnosis 
because of its strong performance on high-dimensional datasets."""


result = chain.invoke({'text' : text})

print(result)

chain.get_graph().print_ascii()
