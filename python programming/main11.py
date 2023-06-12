# file IO 
text=open("file1.txt","wb")
print(text.mode)
print(text.name)
print(text.closed)
text.write(bytes("write this to my file", "UTF-8"))
text.close()    