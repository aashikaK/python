l=[4,2,3,5,6,10]

# squaredList=[]

# for i in l:
#     squaredList.append(i*i)
# print(squaredList)
# This can be done by list comprehension as:
# List comprehension = a short way to create a list using a loop in ONE line.

squaredList=[i*i for i in l]
print(squaredList)