from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# setup RAG vectorstore
loader = TextLoader(r"D:\GenAiProfile\Day3\sample.txt")
documents = loader.load()
chunks = RecursiveCharacterTextSplitter(
    chunk_size=200, chunk_overlap=30
).split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# tool 1 — search your document
@tool
def search_document(query: str) -> str:
    """Search the local document for AI concepts like RAG, embeddings,
    vector databases, Python, LangChain. Use for document questions."""
    docs = retriever.invoke(query)
    return "\n\n".join([d.page_content for d in docs])

# tool 2 — search the web
search = DuckDuckGoSearchRun()

@tool
def search_web(query: str) -> str:
    """Search the internet for current information or general knowledge
    not found in the local document."""
    return search.run(query)

# tool 3 — calculator
@tool
def calculate(expression: str) -> str:
    """Evaluate a math expression like '15 + 27' or '8 * 6'."""
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

tools = [search_document, search_web, calculate]

# LLM + agent
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
agent = create_agent(llm, tools)

def ask_agent(question):
    result = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    return result["messages"][-1].content

# test — agent picks the right tool
questions = [
    "What does the document say about RAG?",
    "What is the current population of Hyderabad?",
    "What is 144 divided by 12?",
    "What does the document say about Python AND what is it generally used for?"
]

for question in questions:
    print(f"\nQ: {question}")
    print(f"A: {ask_agent(question)}")


