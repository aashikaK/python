# Take all items and combine them into a single value

from functools import reduce

nums=[1,2,3,4,5,6]
n=reduce(lambda x,y:x*y,nums)
print(n)