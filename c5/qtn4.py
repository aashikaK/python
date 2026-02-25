s=set()
s.add(20)
s.add(20.0) #20 and 20.2 is same when comparing 20.0 and 20 gives true
s.add('20')
print(len(s))