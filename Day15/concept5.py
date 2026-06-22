from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# load document
loader = TextLoader(r"D:\GenAiProfile\Day3\sample.txt")
documents = loader.load()

# split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,      # max characters per chunk
    chunk_overlap=20,    # overlap between chunks so context isn't lost
    length_function=len
)

chunks = splitter.split_documents(documents)

print(f"Original docs: {len(documents)}")
print(f"Total chunks: {len(chunks)}")
print(f"\nChunk 1: {chunks[0].page_content}")
print(f"\nChunk 2: {chunks[1].page_content}")
print(f"\nMetadata: {chunks[0].metadata}")