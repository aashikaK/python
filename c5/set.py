s={1,2,3,"aas",1} #no duplicates allowed in set
e=set() #creates empty set e={} creates empty dictionary
print(len(s))
s.remove(1)
print(s)
# s.pop() removes random elements since set is unordered..
# s.clear() it makes set empty 

s1={1,2,3,4}
s2={5,6,7,8,4}
print(s1.union(s2))