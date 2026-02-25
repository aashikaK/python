languages={}
for i in range(4):
    name=input("Enter your name: ")
    language=input("Enter your favourite language: ")
    languages.update({name:language})
print(languages)  #or languages.item()


# if keys are same fst one will be updated by the last one but if values are same it wont matter bcz keys are 
# unique identifiers no he values