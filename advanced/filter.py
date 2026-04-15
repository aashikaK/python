# Keep only those items that satisfy a condition
# syntax: filter(function, iterable)

l=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,l))
print(even)