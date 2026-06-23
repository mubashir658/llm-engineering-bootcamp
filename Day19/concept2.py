from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# setup vectorstore
loader = TextLoader(r"D:\GenAiProfile\Day3\sample.txt")
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
chunks = splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# prompt with memory placeholder
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant.
Answer using the context below AND the conversation history.
If answer not in context, say so honestly.

Context: {context}"""),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

# memory store — one per session
store = {}
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# build chain
def get_context(input_dict):
    docs = retriever.invoke(input_dict["question"])
    return "\n\n".join([d.page_content for d in docs])

from langchain_core.runnables import RunnableMap, RunnableLambda

chain = RunnableMap({
    "context": RunnableLambda(get_context),
    "question": RunnableLambda(lambda x: x["question"]),
    "history": RunnableLambda(lambda x: x.get("history", []))
}) | prompt | llm

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

# test with follow-up questions
questions = [
    "What is RAG?",
    "Can you explain that more simply?",
    "What programming language is best for it?"
]

for question in questions:
    print(f"\nQ: {question}")
    response = chain_with_history.invoke(
        {"question": question},
        config={"configurable": {"session_id": "user_1"}}
    )
    print(f"A: {response.content}")