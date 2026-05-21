chunks = ["chunk one", "chunk two", "chunk three"]

with open("output.txt", "w") as f:
    for chunk in chunks:
        f.write(chunk + "\n")  # \n adds a new line after each chunk