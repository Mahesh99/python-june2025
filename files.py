# f=open("3idiots.txt")
# content=f.read()
# print(content)
# f.close()

# we opened file in read mode
# there are 3 modes
# 1. Read mode
# when you open a file in read mode
# - you can only read the file, if file exists
# - the cursor will be placed at the beginning of file
# - it will throw an error
# 2. Write mode
# 3. Append mode

# f=open("3idiots.txt")
# content=f.readline()
# print(content)
# content=f.readline()
# print(content)
# f.close()



# f=open("3idiots.txt")
# content=f.readlines()
# print(content[5])
# f.close()

# write mode
# When you open a file in write mode
# - it will check if file exists, if file exists it will empty the file and places the cursor at the beginning
# - if there no file, it will create new file and places cursor at beginning
# - you can only write in write mode
# you can write the content into the file
# f=open("ashfaq.txt","w")
# f.write("hello")
# f.close()



# f=open("ashfaq.txt","w")
# data=["hello world","hello","hi"]
# f.writelines(data)
# f.close()



# append mode
# f=open("manuraj.txt","a")
# f.write("This is new line")
# f.close()

f=open("manuraj.txt","a")
data=["hello world","hello","hi"]
f.writelines(data)
f.close()

f=open("manuraj.txt")
print(f.read())
f.close()