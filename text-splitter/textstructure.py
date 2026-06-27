from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

text = """
Text structure-based text splitting is a technique that divides a document based on its 
natural structure, such as paragraphs, headings, sections, sentences, or code blocks, 
instead of splitting it by a fixed number of characters or tokens. This helps preserve 
the meaning and context of the content, making it more suitable for processing by large language models (LLMs).
For example, instead of cutting a paragraph in the middle after 500 characters, a text structure-based splitter 
keeps the entire paragraph or section together. In LangChain, classes like RecursiveCharacterTextSplitter, 
MarkdownHeaderTextSplitter, and HTMLHeaderTextSplitter are commonly used for structure-based splitting."""


result = splitter.split_text(text)

print(result)
