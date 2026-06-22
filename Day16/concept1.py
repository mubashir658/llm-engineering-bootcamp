from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv()

model=SentenceTransformer("all-miniLM-L6-v2")
sentences=[
    "What is a vector database?",
    "Vector databases store embeddings for similarity search",
    "Python is a programming language",
    "ChromaDB is a vector store"
]
embeddings=model.encode(sentences)

print(f"Number of embeddings:{len(embeddings)}")
print(f"embedding size:{len(embeddings[0])}dimensions")
print(f"First embedding preview:{embeddings[0][0:5]}")