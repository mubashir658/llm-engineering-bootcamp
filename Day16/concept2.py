from sentence_transformers import SentenceTransformer
import chromadb
client=chromadb.Client()
collection=client.create_collection("first_collection")
model=SentenceTransformer("all-MiniLM-L6-v2")
documents=[
    "What is a vector database?",
    "Vector databases store embeddings for similarity search",
    "Python is a programming language",
    "ChromaDB is a vector store"
]
embeddings=model.encode(documents).tolist()
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[f"doc_{i}" for i in range(len(documents))]
)

query="what is python?"
query_embedding=model.encode([query]).tolist()
result=collection.query(
    query_embeddings=query_embedding,
    n_results=2
)
print(f"\nQuery: {query}")
print("\n top two most similar embeddings")
for doc in result["documents"][0]:
    print(f"->{doc}")
