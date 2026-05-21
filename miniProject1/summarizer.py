# from dotenv import load_dotenv
# import os 
# load_dotenv()

# def load_config():
#     key=os.getenv("OPENAI_API_KEY")
#     if not key:
#         raise ValueError("OPENAI_API_KEY missing from .env file")
#     name=os.getenv("MODEL_NAME")
#     try:
#         tokens=int(os.getenv("MAX_TOKENS"))
#     except:
#         print("using default tokens 1000")
#         tokens=1000
#     response={"key":key,
#               "name":name,
#               "tokens":tokens}
#     return response

# config=load_config()
# print(config)




# def chunk_text(filepath,chunk_size=20):
#     with open(filepath,"r") as f:
#         content=f.read()
#     words=content.split()
#     chunks=[" ".join(words[i:i+chunk_size]) for i in range(0,len(words),chunk_size)]
#     return chunks
# chunks=chunk_text(r"D:\GenAiProfile\Day3\sample.txt",chunk_size=20)
# print(f"total chunks:{len(chunks)}")
# for i,chunk in enumerate(chunks):
#     print(f"\nchunk{i+1}:{chunk}")



# def summarize_chunk(chunk):
#     sentences=chunk.split(".")
#     sentences=[s.strip() for s in sentences if s.strip()]
#     if not sentences:
#         return "No contnet"
#     return sentences[0]+"."
# chunks=chunk_text(r"D:\GenAiProfile\Day3\sample.txt",chunk_size=20)
# for i,chunk in enumerate(chunks):
#     summary=summarize_chunk(chunk)
#     print(f"\nchunk{i+1}:")
#     print(f"Full: {chunk}")
#     print(f"summary:  {summary}")



# def main():
#     # Step 1 — load config
#     config = load_config()
#     print(f"Using model: {config['name']}\n")

#     # Step 2 — chunk the file
#     chunks = chunk_text(r"D:\GenAiProfile\Day3\sample.txt", chunk_size=20)
#     print(f"Total chunks: {len(chunks)}\n")

#     # Step 3 — summarize each chunk
#     results = []
#     for i, chunk in enumerate(chunks):
#         summary = summarize_chunk(chunk)
#         results.append({
#             "chunk": i + 1,
#             "original": chunk,
#             "summary": summary
#         })
#         print(f"Chunk {i+1} done ✓")

#     # Step 4 — save to output file
#     with open("summary_output.txt", "w") as f:
#         for r in results:
#             f.write(f"=== Chunk {r['chunk']} ===\n")
#             f.write(f"Original : {r['original']}\n")
#             f.write(f"Summary  : {r['summary']}\n\n")

#     print(f"\nDone! Saved {len(results)} summaries to summary_output.txt")

# main()




from dotenv import load_dotenv
import os

load_dotenv()

def load_config():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY missing from .env file")
    name = os.getenv("MODEL_NAME")
    try:
        max_tokens = int(os.getenv("MAX_TOKENS"))
    except ValueError:
        print("MAX_TOKENS invalid, using default 1000")
        max_tokens = 1000
    return {"api_key": key, "model": name, "max_tokens": max_tokens}

def chunk_text(filepath, chunk_size=20):
    with open(filepath, "r") as f:
        content = f.read()
    words = content.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def summarize_chunk(chunk):
    sentences = chunk.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return "No content"
    return sentences[0] + "."

def main():
    config = load_config()
    print(f"Using model: {config['model']}\n")
    chunks = chunk_text(r"D:\GenAiProfile\Day3\sample.txt", chunk_size=20)
    print(f"Total chunks: {len(chunks)}\n")
    results = []
    for i, chunk in enumerate(chunks):
        summary = summarize_chunk(chunk)
        results.append({"chunk": i+1, "original": chunk, "summary": summary})
        print(f"Chunk {i+1} done ✓")
    with open("summary_output.txt", "w") as f:
        for r in results:
            f.write(f"=== Chunk {r['chunk']} ===\n")
            f.write(f"Original : {r['original']}\n")
            f.write(f"Summary  : {r['summary']}\n\n")
    print(f"\nDone! Saved {len(results)} summaries to summary_output.txt")

main()
