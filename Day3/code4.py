def chunk_and_save(filepath,chunk_size=20):
    with open(filepath,"r") as f:
        content=f.read()
    words=content.split()
    chunks=[words[i:i+chunk_size] for i in range(0,len(words),20)]
    with open("chunks.txt","w") as f2:
        for chunk in chunks:
            f2.write(" ".join(chunk)+"\n")
    return len(chunks)


count=chunk_and_save(r"D:\GenAiProfile\Day3\sample.txt",chunk_size=20)
print(f"created {count} chunks")
