from langchain.text_splitter import RecursiveCharacterTextSplitter , Language

text = """
import time

# Count down from 3 to 1
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)  # Pause for 1 second

print("Blast off! 🚀")"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=50,
    chunk_overlap= 0
)

result = splitter.split_text(text)
print(result[0])