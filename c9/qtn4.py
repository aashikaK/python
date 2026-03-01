with open("c9/donkey.txt","r") as f:
    text=f.read()
text= text.replace("donkey","#####")
    
with open("c9/donkey.txt","w") as f:
    f.write(text)
print("Successfully replaced 'donkey' with '#####'")