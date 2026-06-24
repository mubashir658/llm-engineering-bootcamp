from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# setup vectorstore
loader = TextLoader(r"D:\GenAiProfile\Day3\sample.txt")
documents = loader.load()
chunks = RecursiveCharacterTextSplitter(
    chunk_size=200, chunk_overlap=30
).split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# tools
@tool
def search_document(query: str) -> str:
    """Search the local document for AI concepts."""
    docs = retriever.invoke(query)
    return "\n\n".join([d.page_content for d in docs])

@tool
def calculate(expression: str) -> str:
    """Evaluate a math expression."""
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

tools = [search_document, calculate]

# agent
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
agent = create_agent(llm, tools)

# memory store
store = {}
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# wrap agent with memory
# wrap agent with memory
agent_with_memory = RunnableWithMessageHistory(
    agent,
    get_session_history,
    input_messages_key="messages"
)
# test with follow-up questions
conversations = [
    "What does the document say about Python?",
    "Can you give more details about that?",
    "What is 25 multiplied by 4?",
    "What was the first thing I asked you?"
]

for question in conversations:
    print(f"\nQ: {question}")

    result = agent_with_memory.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        },
        config={"configurable": {"session_id": "user_1"}}
    )

    print(f"A: {result['messages'][-1].content}")