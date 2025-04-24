set={1,2,3,True,"apple"}  # true s 1 which is duplicate value so its not set tbh
print(set)

# set[0] not allowed because the values are is unordered 
set.add(8)
set.remove(2) 
set.discard(55)
set.pop()


set1={3,6,8,62}
set2={77,"a",89}
print(set)
print(set1)
print(set2)

print(set1.union(set2)) #or use set1 | set2
print (set1.intersection(set2)) #or use set1 & set2