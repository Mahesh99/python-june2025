# STRING METHODS EXPLANATIONS WITH EXAMPLES

# 1. split()
# Used to split a string into a list based on a delimiter (default is space)
text = "apple,banana,cherry"
print("Original String:", text)
print("After split():", text.split(","))  # ['apple', 'banana', 'cherry']

# 2. strip()
# Removes whitespace from the beginning and end of a string
s = "   Hello World!   "
print("Original with spaces:", repr(s))
print("After strip():", repr(s.strip()))  # 'Hello World!'

# 3. replace()
# Replaces all occurrences of a substring with another string
s2 = "I like Python. Python is easy."
print("Original:", s2)
print("After replace():", s2.replace("Python", "Java"))  # 'I like Java. Java is easy.'

print("\n" + "-"*40 + "\n")

# LIST METHODS EXPLANATIONS WITH EXAMPLES

# 4. append()
# Adds an element to the end of the list
fruits = ["apple", "banana"]
fruits.append("cherry")
print("After append('cherry'):", fruits)  # ['apple', 'banana', 'cherry']

# 5. insert()
# Inserts an element at a specific index
fruits.insert(1, "orange")
print("After insert(1, 'orange'):", fruits)  # ['apple', 'orange', 'banana', 'cherry']

# 6. remove()
# Removes the first occurrence of the specified value
fruits.remove("banana")
print("After remove('banana'):", fruits)  # ['apple', 'orange', 'cherry']


# STRING METHODS
s = " Hello, Python! "

print("Original String:", s)
print("Strip:", s.strip())
print("Lower:", s.lower())
print("Upper:", s.upper())
print("Title:", s.title())
print("Replace:", s.replace("Python", "World"))
print("Split:", s.split(","))
print("Find 'Python':", s.find("Python"))
print("Count 'o':", s.count("o"))

print("\n" + "-"*40 + "\n")

# STRING SLICING
text = "Programming"
print("Original String:", text)
print("text[0:6]:", text[0:6])
print("text[:4]:", text[:4])
print("text[4:]:", text[4:])
print("text[-1]:", text[-1])
print("text[::-1] (Reversed):", text[::-1])

print("\n" + "-"*40 + "\n")

# LIST CREATION
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

# LIST UPDATION
fruits.append("orange")
print("After append:", fruits)

fruits[1] = "blueberry"
print("After update:", fruits)

fruits.insert(1, "grape")
print("After insert at index 1:", fruits)

del fruits[2]
print("After deleting index 2:", fruits)

fruits.remove("grape")
print("After removing 'grape':", fruits)

print("\n" + "-"*40 + "\n")

# LIST SLICING
numbers = [10, 20, 30, 40, 50, 60]
print("Original Numbers:", numbers)
print("numbers[1:4]:", numbers[1:4])
print("numbers[:3]:", numbers[:3])
print("numbers[3:]:", numbers[3:])
print("numbers[::-1]:", numbers[::-1])

print("\n" + "-"*40 + "\n")

# EXERCISES (Uncomment to try)

# 1. Replace "Python" with your name in the string below.
# my_string = "Hello, Python!"

# 2. Slice the string "DataScience" to get "Data" and "Science"
# s = "DataScience"

# 3. Create a list of 5 colors and print the 2nd and 4th colors

# 4. Reverse the string "Machine"
# word = "Machine"

# 5. Replace the 3rd item in a list with "kiwi"
# fruits = ["apple", "banana", "cherry", "orange"]
