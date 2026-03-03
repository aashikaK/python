with open("c9/this.txt") as f:
    content=f.read()

with open("c9/this_copy.txt","W") as f:
    f.write(content)