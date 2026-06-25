from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

#chat template

chat_template = ChatPromptTemplate([
    ('system' , 'you are a helpful assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human' , '{query}')
])

#load the chat history
chat_history = []

with open('chat_history.txt') as f:
    chat_history.append(f.readlines())

print(chat_history)


#create prompt
chat_template.invoke({'chat_history' : chat_history,'query':'where is my refund'})