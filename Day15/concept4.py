from langchain_community.document_loaders import TextLoader
loader=TextLoader(r"D:\GenAiProfile\Day3\sample.txt")
documents=loader.load()

print(f"Total Docs:{len(documents)}")
print(f"content_preview:{documents[0].page_content[:20]}")
print(f"Metadata:{documents[0].metadata}")
