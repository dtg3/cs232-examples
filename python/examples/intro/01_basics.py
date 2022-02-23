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
my_variable = 10
print(my_variable)

# I can also change what this variable holds and
# the type of data it holds at any time.
my_variable = "Hello"
print(my_variable)

# While this can make for easy coding it can create
# some pitfalls. If I assume that my_variable is still
# holding a numeric value and try to do an operation
# that is not supported by a string, the program will
# crash.
# Example: print(my_variable / 10)

# Worse yet, I might do a compatible operation and get
# an incorrect result. Be careful of this.
print(my_variable * 2)


# In the above statments, I've used python's print
# function which has a variety of uses:

# We can simply print a single literal value or a variable.
print("String literal")
print(10)
print(my_variable)

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
my_empty_list = [] 
print(my_empty_list)

# A list initialized with items
my_list = [1, 2, 3]
print(my_list)

# Lists can have different types
my_various_items = [1, 3, "String", 2.1]
print(my_various_items)

# Get the item at index 1
print(my_various_items[1])

# Add an item to the end of the list
my_various_items.append("new item")
print(my_various_items)

# Remove and return the last item from the list
print(my_various_items.pop()) 
print(my_various_items)

# Insert an item at an index
my_various_items.insert(1, "inserted item")
print(my_various_items)

# Remove and return the item at the specific index from the list
print(my_various_items.pop(1))
print(my_various_items)

# Remove an item by value from a list (does not return anything)
my_various_items.remove(2.1)
print(my_various_items)

# Clear the contents of a list
print(my_list)
my_list.clear()
print(my_list)

# Delete a list
print(my_list)
del my_list # The list can no longer be used once deleted
# print(my_list) # This will cause an error

# Tuples are similar to lists, but they are immutable and cannot change

# Empty Tuple for illustrative purposes. An empty tuple would most likely
# indicate an empty result for an operation where the result should
# be immutable.
my_empty_tuple = ()
print(my_empty_tuple)

# Initialized Tuple
my_tuple = (1, "word", 4, "you")
print(my_tuple)

# Access elements of the tuple
print(my_tuple[2])

# A tuple with only one item has special syntax
my_single_tuple = ("one item only",) # note the trailing comma
print(my_single_tuple)

# Dictionaries store data in key, value pairs
# Empty dictionary
myEmptyDictionary = {}
print(myEmptyDictionary)

# Initialized Dictionary
# key:value
my_dictionary = { 10:"foo", 14:"bar", "baz":40 }
print(my_dictionary)

# Add an item to the dictionary
my_dictionary["new item"] = "I'm new!"
print(my_dictionary)

# Change an item in the dictionary
my_dictionary["new item"] = "I'm and updated item!"
print(my_dictionary)
my_dictionary.update({50:"I'm updated with a function!"})
print(my_dictionary)

# Access a data item by its key
# Use this method if you are SURE that the
# data is in the dictionary or you get an error.
print(my_dictionary["baz"])
print(my_dictionary[14])
# Alternatively, you can use the get function 
# and provide the key. This is safer as it does
# not throw an error if the key in the dictionary.
print(my_dictionary.get(10)) # Returns the value
print(my_dictionary.get("foobar")) # Returns None (key not there) 
# None can be considered the equivalent of NULL is C/C++

# Get a list of all the keys in a dictionary
print(my_dictionary.keys())

# Get a list of key, value pairs stored in a tuple
print(my_dictionary.items())

# Sets are like lists, but they have some special rules.
# 1. They cannot contain duplicate items
# 2. Items cannot be changed, but they can be added or removed
# 3. No guaranteed order
# 4. Items are not indexable

# Empty Set
my_empty_set = {}
print(my_empty_set)

# Initialized Set
my_set = {"bread", "milk", "eggs"}
print(my_set)

# Add an item to the set
my_set.add("grape")
print(my_set)

# Add multiple items from a list
itemList = ["lemons", "donuts"]
my_set.update(itemList)
print(my_set)

# Remove an item
my_set.remove("donuts") # Will cause an error if the item isn't in the list
print(my_set)
my_set.discard("donuts") # Removes an item WITHOUT causing an error
