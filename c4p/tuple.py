tup=(1,2,3,4,5)
# a,b=tup   gives error:too many values to unpack
a,b, *rest= tup
print(a,b)