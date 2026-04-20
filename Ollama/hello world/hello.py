from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama


@tool
def sayHello(query: str):
    """Just returns Hello World no matter the input is"""
    # return "Hello World"


llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)

agent = create_agent(llm, tools=[sayHello])

result = agent.invoke("Hi there!")
print(result)
