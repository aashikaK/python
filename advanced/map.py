# Apply a function to every item in a list

num=[1,2,3,4,5,6,7]

# def double(x):
#     return x * 2

# result = map(double, nums)  #(function,iterable)
# print(list(result))

# with lambda same::
sum=map(lambda x:x+1,num)
print(list(sum))

# for strings
names = ["ram", "shyam", "hari"]

result = list(map(lambda x: x.upper(), names))
print(result)

# Use when:

# Same operation on all elements
# Simple transformation