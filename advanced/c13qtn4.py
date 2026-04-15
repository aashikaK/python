# mul=[7,14,21,27,35,42,49,56,63,70]

table=[str(7*i for i in range(1,11))]  #str bcz join fnction needs list of string

s="\n".join(table)
print(s)