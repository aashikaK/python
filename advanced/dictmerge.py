# Merge Operator (|) Combines two dictionaries into a new dictionary

d1={"a":1,"b":2}
d2={"b":7,"c":3} 
result=d1|d2 #right side dictionary d2's b overlaps d1's b and b becomes 7
print(result)

# Update Operator (|=) Updates the original dictionary
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d1 |= d2
print(d1)