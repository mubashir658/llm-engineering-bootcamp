from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
from dotenv import load_dotenv
import os

load_dotenv()
#initializing everything
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
embedding_model=SentenceTransformer("all-MiniLM-L6-v2")
chroma_client=chromadb.PersistentClient('./rag_db')
collection=chroma_client.get_or_create_collection('rag_collection')




#load and chunk
def load_and_chunk(filepath):
    loader=TextLoader(filepath)
    documents=loader.load()
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30
    )
    chunks=splitter.split(documents)
    print(f"loaded {len(documents)} documents and {len(chunks)} chunks" )
    return chunks

# embed_and_store
def embed_and_store(chunks):
    if collection.count()>0:
        print(f"collection already has {collection.count()} chunks -skipping embeddings")
        return
    texts=[chunk.page_content for chunk in chunks]
    embeddings=embedding_model.encode(texts).tolist()
    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=[f"doc_{i}"for i in range(len(texts))]
    )
    print(f"added {collection.count()} chunks in collection")
def retrive(query,n_result=3):
    query_embedding=embedding_model.encode([query]).tolist()
    result=collection.query(
        query_embeddigns=query_embedding,
        n_results=n_result
    )
    return result["documents"][0]


def generate_answer(query,context_chunks):
    context=[f"chunk{i+1}:{chunk}" for i,chunk in enumerate(context_chunks)]
    prompt=ChatPromptTemplate([
        ("system","""you are a helpful assistant .provide the answer from the given context . If answer is not there then provide"I don't know based on the given context"
         context:{context}"""),
        ("human","{question}")
    ])
    chain=prompt|llm
    response=chain.invoke(
        {
            "context":context,
            "question":query
        }
    )
    return response.content
def rag_pipeline(filepath,query):
    print("\n"+"="*50)
    print(f"Query:{query}")
    print("="*50)
    #step 1 load and chunk
    chunks=load_and_chunk(filepath)
    #step2 embed and store
    embed_and_store(chunks)
    #retrive
    print("\nRetrieving relevant chunks...")
    relevant_chunks=retrive(query)
    print(f"Found {len(relevant_chunks)} relevant chunks")
    for i,chunk in enumerate(relevant_chunks):
        print(f"chunk{i+1}:{chunk[:80]}....")
    
    # answer 
    print("\n generating answer")
    answer=generate_answer(query,relevant_chunks)
    print(f"\nAnswer: {answer}")
    return answer

# run it
if __name__ == "__main__":
    filepath = r"D:\GenAiProfile\Day3\sample.txt"
    
    # test with 3 different questions
    questions = [
        "What is RAG?",
        "What programming language is best for AI?",
        "What are vector databases used for?"
    ]
    
    for question in questions:
        rag_pipeline(filepath, question)
        print("\n" + "-"*50)



