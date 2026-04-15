# Keep only those items that satisfy a condition
# syntax: filter(function, iterable)

list=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,list))
print(even)