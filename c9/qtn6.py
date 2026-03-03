with open("c9/log.txt") as f:
    content=f.read()

if("python" in content):
    print("Yes python is in content")
else:
    print("Python is not present in content")