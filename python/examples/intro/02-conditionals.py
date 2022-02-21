"""Python Conditionals

Demonstration of python comparison
operators, logical operators, membership
operators, and conditionals.
"""


# Standard comparison operators are used
# in Python.
x = 10
print(x < 5)
print(x > 5)
print(x <= 5)
print(x >= 5)
print(x != 5)
print(x == 5)

# Python also has some nice shorthand 
# for comparison operators
print(2 > x < 5)
print(9 <= x >= 5)

# Standard logical operators are used
# in Python.
print(x > 5 and x <= 6)
print(x > 5 or x != 6)
print(not (x < 20)) 

# For things like collections (lists,
# dictionaries, tuples, sets, and strings, etc.)
# we can check if items are present in the 
# collection.
myExampleList = ["apple", "banana", "grape", "pineapple"]
print("grape" in myExampleList)
print("hotdog" in myExampleList)
print("grape" not in myExampleList)
print("hotdog" not in myExampleList)

# Conditional statements are similar to those in C/C++
# but with different syntax.
# Simple if
if 'grape' in myExampleList:
    print("Item in the list")

# Simple if else
if 'hotdog' in myExampleList:
    print("Item in the list")
else:
    print("Item not in the list")

# Multiple conditional if statement
if 'grape' in myExampleList:
    print("Purple Fruit")
elif 'banana' in myExampleList:
    print("Yellow Fruit")
elif 'pineapple' in myExampleList:
    print("Spiky Fruit")
else:
    print("Red Fruit")
    