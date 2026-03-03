words=['Donkey','Bad' ,'Dirty' ]
words= words.lower()


with open("c9/cencored.txt","r") as f:
    text=f.read()

for word in words:
    text= text.replace(word,"#"*len(word))
    text = text.replace(word.lower(), "#" * len(word))
    text = text.replace(word.upper(), "#" * len(word))
    # for word in words:
    # pattern = re.compile(word, re.IGNORECASE)
    # text = pattern.sub("#" * len(word), text)

with open("c9/donkey.txt","w") as f:
    f.write(text)
print("Successfully replaced 'donkey' with '#####'")