with open(r"D:\GenAiProfile\Day3\sample.txt","r") as f:
    l=f.readlines()
lines = [line.strip() for line in l]
output=[line for line in lines if "AI" in line]
print(output)
   

