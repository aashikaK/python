st="Hi, this is Aashika Khatiwada aka AK the don. Haha, jokes apart, tell me how was your day?"
str="I hope it was good."
file=open("c9/myFile.txt", "a")
file.write(str)
print('Successfully carried out append operation..')
file.close()

# if we write again in the file that already has text it "w" will replace previous content with the new content