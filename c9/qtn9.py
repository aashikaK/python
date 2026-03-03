with open("c9/this.txt") as f:
    data1=f.read()
with open("c9/this_copy.txt") as f:
    data2=f.read()
if(data1==data2):
    print("The conttent of 'this.txt' matches with 'this_copy.txt'")
    
else:
      print("The conttent of 'this.txt' does not matche with 'this_copy.txt'")


# simply do f.write('') for the file you want to clear contents of then it will complete qtn10