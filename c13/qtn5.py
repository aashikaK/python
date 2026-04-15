from functools import reduce

n = [3, 45, 6778, 1, 23, 45, 988, 67]

def max(a,b):
    if(a>b):
        return a
    else:
        return b

result = reduce(max, n)

print(result)