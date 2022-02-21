"""Python Basics

This program introduces some of the basics
of the python programming language. The first
thing you will notice is this is a docstring.
Docstrings are comments that are meant to be
used at the top of files, classes, or below
function definitions to generate documentation.
"""


# Any line that begins with a hashtag is a comment.
# It is best practice to use the hashtag instead of
# the """ (triple quote) for the docstring when you
# need a multiple line comment that you DO NOT want
# to be a docstring. Your VS code editor helps with
# this by autofilling hashtags after a few lines when
# you press the enter key to make a new line. If you
# have a bunch of text you want to turn into a comment
# you can also highlight that text with your mouse and
# use CTRL/CMD + / to comment out the selection.


# Python does not use static typing for variables.
# Instead, variables are Dynamically Typed, which
# means that a variables type depends on what
# is being stored within in it a any give time.
# Here I can have an integer 10.
myVariable = 10
print(myVariable)

# I can also change what this variable holds and
# the type of data it holds at any time.
myVariable = "Hello"
print(myVariable)

# While this can make for easy coding it can create
# some pitfalls. If I assume that myVariable is still
# holding a numeric value and try to do an operation
# that is not supported by a string, the program will
# crash.
# Example: print(myVariable / 10)

# Worse yet, I might do a compatible operation and get
# an incorrect result. Be careful of this.
print(myVariable * 2)


# In the above statments, I've used python's print
# function which has a variety of uses:

# We can simply print a single literal value or a variable.
print("String literal")
print(10)
print(myVariable)

# We can also print multiple literal values or variables.
print("Hello", "World!")
print("Score:", 10)

# By default the comma separated parameters to print are
# displayed with space separation...but we can change that
# to anything using the named parameter sep.
print("Hello", "World!", sep="-")
print("Score:", 10, sep="==>")

# The print function normally outputs a newline character
# (\n) after outputting all parameters. This too can be
# changed using the named paramter end.
print("Hello", "World", sep=" ", end=", ")
print("Good to see you", end="!\n")

# Note that these named parameters must appear AFTER all of
# the other unnamed parameters.


# Python features most of the standard mathematical operations
# you have seen in most of the languages you have used so far
# but a few you might not have seen (or in a different format).
print(3 + 1)  # Addition
print(3 - 1)  # Subtraction
print(3 * 1)  # Multiplication
print(3 ** 2) # Exponents (3^2)
print(3 / 2)  # Division always produces a float
print(6 / 2)  
print(3 // 2) # Floor division (produces an integer)
print(17 % 3)  # Modulus division (remainder)

# Some of these same operators can be used for string manipulation
print("String " + "Addition") # Concatination
print("Repeat" * 4)           # Repeating strings

# While on the topic...Strings in Python are immutable
# meaning they can't be changed. Each time you manipulate
# a string, you actually get a brand new string (this
# includes concatination and multiplication).


# Along with numbers and strings we have a few different
# types of collections to hold our data:

# Lists which work very similarly to arrays.
# Empty list
myEmptyList = [] 
print(myEmptyList)

# A list initialized with items
myList = [1, 2, 3]
print(myList)

# Lists can have different types
myVariousItems = [1, 3, "String", 2.1]
print(myVariousItems)

# Get the item at index 1
print(myVariousItems[1])

# Add an item to the end of the list
myVariousItems.append("new item")
print(myVariousItems)

# Remove and return the last item from the list
print(myVariousItems.pop()) 
print(myVariousItems)

# Insert an item at an index
myVariousItems.insert(1, "inserted item")
print(myVariousItems)

# Remove and return the item at the specific index from the list
print(myVariousItems.pop(1))
print(myVariousItems)

# Remove an item by value from a list (does not return anything)
myVariousItems.remove(2.1)
print(myVariousItems)

# Clear the contents of a list
print(myList)
myList.clear()
print(myList)

# Delete a list
print(myList)
del myList # The list can no longer be used once deleted
# print(myList) # This will cause an error

# Tuples are similar to lists, but they are immutable and cannot change
# Empty Tuple
myEmptyTuple = ()
print(myEmptyTuple)

# Initialized Tuple
myTuple = (1, "word", 4, "you")
print(myTuple)

# Access elements of the tuple
print(myTuple[2])

# A tuple with only one item has special syntax
mySingleTuple = ("one item only",) # note the trailing comma
print(mySingleTuple)

# Dictionaries store data in key, value pairs
# Empty dictionary
myEmptyDictionary = {}
print(myEmptyDictionary)

# Initialized Dictionary
# key:value
myDictionary = { 10:"foo", 14:"bar", "baz":40 }
print(myDictionary)

# Add an item to the dictionary
myDictionary["new item"] = "I'm new!"
print(myDictionary)

# Change an item in the dictionary
myDictionary["new item"] = "I'm and updated item!"
print(myDictionary)
myDictionary.update({50:"I'm updated with a function!"})
print(myDictionary)

# Access a data item by its key
# Use this method if you are SURE that the
# data is in the dictionary or you get an error.
print(myDictionary["baz"])
print(myDictionary[14])
# Alternatively, you can use the get function 
# and provide the key. This is safer as it does
# not throw an error if the key in the dictionary.
print(myDictionary.get(10)) # Returns the value
print(myDictionary.get("foobar")) # Returns None (key not there) 
# None can be considered the equivalent of NULL is C/C++

# Get a list of all the keys in a dictionary
print(myDictionary.keys())

# Get a list of key, value pairs stored in a tuple
print(myDictionary.items())

# Sets are like lists, but they have some special rules.
# 1. They cannot contain duplicate items
# 2. Items cannot be changed, but they can be added or removed
# 3. No guaranteed order
# 4. Items are not indexable

# Empty Set
myEmptySet = {}
print(myEmptySet)

# Initialized Set
mySet = {"bread", "milk", "eggs"}
print(mySet)

# Add an item to the set
mySet.add("grape")
print(mySet)

# Add multiple items from a list
itemList = ["lemons", "donuts"]
mySet.update(itemList)
print(mySet)

# Remove an item
mySet.remove("donuts") # Will cause an error if the item isn't in the list
print(mySet)
mySet.discard("donuts") # Removes an item WITHOUT causing an error
