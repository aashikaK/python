d={} #empty dictionary

marks={"Sita":100,
       "Mina":22,
       "Aashish":78
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Sita":99,"Alina":56})
print(marks)

print(marks.get("Harry")) #returns none
print(marks["Harry"]) #returns error
print(marks.get('Sita'))