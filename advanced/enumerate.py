l=[4,5,6,7,8,98]

# index=0
# for i in l:
#     print(f"The item in index {index} is {i}")
#     index+=1

# This can be simplified using enumerate function

for index,item in enumerate(l):
    print(f"The item in index {index} is {item}")