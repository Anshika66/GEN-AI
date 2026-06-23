from langchain.chat_models import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()


model = ChatAnthropic(model = "claude-3.5" , temperature = 0)
result = model.invoke("what is the level of water in delhi?")

print(result.content)