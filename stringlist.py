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
