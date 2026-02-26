def rem_strip(list,word):
    n=[]
    for item in list:
       if not(item==word):
           n.append(item.strip(word))
    return n

l=["apple", "banana","kiwi","orange","an"]
print(rem_strip(l,"an"))