st="Hi, this is Aashika Khatiwada aka AK the don. Haha, jokes apart, tell me how was your day?"
str="I hope it was good."
file=open("c9/myFile.txt", "a")
file.write(str)
print('Successfully carried out append operation..')

# data=file.readlines()   for reading and appending we need to open on a+ mode no just a mode
# print(data)
# file.close()