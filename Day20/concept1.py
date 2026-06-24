from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# define tools
@tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@tool
def get_ai_fact(topic: str) -> str:
    """Get a fact about an AI topic like RAG, LangChain, embeddings."""
    facts = {
        "rag": "RAG stands for Retrieval Augmented Generation.",
        "langchain": "LangChain is a framework for LLM applications.",
        "embeddings": "Embeddings convert text into numerical vectors."
    }
    return facts.get(topic.lower(), f"No fact found for {topic}")

tools = [add_numbers, get_ai_fact]

# create agent — modern LangGraph way
agent = create_react_agent(llm, tools)

# run it
def ask_agent(question):
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    return result["messages"][-1].content

# test
questions = [
    "What is 15 + 27?",
    "Tell me a fact about RAG",
    "What is 8 + 6 and tell me about embeddings?"
]

for question in questions:
    print(f"\nQ: {question}")
    print(f"A: {ask_agent(question)}")