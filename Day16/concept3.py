#persistent chromadb storage

from sentence_transformers import SentenceTransformer
import chromadb
model=SentenceTransformer("all-MiniLM-L6-v2")

client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_or_create_collection("genai_docs")
if collection.count()==0:
    documents = [
        "RAG stands for Retrieval Augmented Generation",
        "ChromaDB is a vector database for storing embeddings",
        "LangChain connects LLMs with external data sources",
        "Python is the most popular language for AI development",
        "Embeddings convert text into numerical vectors"
    ]
    embedding=model.encode(documents).tolist()
    collection.add(
        documents=documents,
        embeddings=embedding,
        ids=[f"doc_{i}"for i in range(len(documents))]
    )
    print(f"added {len(documents)} documents")
else:
    print(f"loaded {collection.count()} existing documents")
query="why python is popular?"
query_embedding=model.encode([query]).tolist()
result=collection.query(
    query_embeddings=query_embedding,
    n_results=2
)
print(f"\nQuery: {query}")
print("\ntop 2 matching embeddings:")
for doc in result["documents"][0]:
    print(f"->{doc}")
