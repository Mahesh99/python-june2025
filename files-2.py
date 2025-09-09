# # mode r w a 
# f=open("palindrome.py","r")
# x=f.read()
# print(x)
# f.close

# f=open("name.txt","r")
# x=f.read()
# print(x)
# f.close

# f=open("name.txt","w")
# x=f.write()
# print(x)
# f.close

# f=open("names.txt","w")
# x=f.write("ABHI" " RISHI")
# print(x)
# f.close

# f=open("hello.txt")
# lines=f.readlines()
# print(lines[3])
# f.close()

# r+, w+, a+
# f=open("hello.txt","r+")
# # print(f.read())
# f.write("this is another line")
# f.close()

# f=open("hello2.txt","w+")
# f.write("this is a line")
# # f.seek(5)
# print(f.tell())
# # print(f.read())
# f.close()


# f=open("hello3.txt","a")
# print(f.tell())
# # f.write("hello this is a new line\n")
# f.seek(0)
# # print(f.read())
# print(f.readable(),f.writable())
# f.close()


# f=open("somefile.txt","w")
# lines=["hi\n",'hello\n','world\n','this is some line\n']
# lines.sort()
# # print(lines)
# f.writelines(lines)
# f.close()

f=open("somefile.txt","r")
data=f.readlines()
f.close()

print(data)
data.sort()

f=open("somefile.txt","w")
f.writelines(data)
f.close()


