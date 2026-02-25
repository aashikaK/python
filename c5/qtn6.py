languages={}
for i in range(4):
    name=input("Enter your name: ")
    language=input("Enter your favourite language: ")
    languages.update({name:language})
print(languages)  #or languages.item()