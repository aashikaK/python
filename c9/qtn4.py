with open("c9/donkey.txt","w+") as f:
    text=f.read()
    for "donkey" in text.lower():
       text= text.replace("donkey","#####")
    f.write(text)