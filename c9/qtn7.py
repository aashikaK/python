with open("c9/qtn7") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f"Yes, python is present in. Line no: {lineno}")
        break
        lineno+=1
        