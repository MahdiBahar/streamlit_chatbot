from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage


# initiate the model
# llm = ChatOllama(
#     model="phi4:latest",
#     temperature=0

# )
from langchain_ollama import OllamaLLM

# Specify the remote server's URL
llm = OllamaLLM(model="phi4:latest", base_url="http://127.0.0.1:11434")


# initiate the 'messages' object
messages = [
    SystemMessage("Act like a Pirate"),
    HumanMessage("Hi, how are you today?"),
]

# execute the model (with messages)
result = llm.invoke(messages)


#show result in the screen
print(result)


############################################################



