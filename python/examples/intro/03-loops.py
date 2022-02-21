"""Python Looping

Demonstration of python looping
with iteratable structures and conditionals
"""


# For loops in Python are a bit different than
# C/C++ for loops as they use for each semantics.
# Below we use the range function to create an
# iterable collection of numbers.

# "number" is just a variable here that holds a
# value from the collection for each iteration of
# the for loop.
for number in range(10):
    print(number)

# Also works with strings as they are an iterable type
for letter in "text":
    print(letter)

# Works with all containers, but only list and
# dictionary are shown. Tuples and sets work
# similar to a list.
# Iterating through a list
myList = ["apple", "banana", "cherry", "pineapple", "strawberry"]
for item in myList:
    print(item)

# Iterating over a dictionary by keys
myDictionary = { 10:"foo", 20:"bar", 30:"baz"}
for key in myDictionary:
    print(key, '->', myDictionary[key])

# Or we can iterate over the dictionary as a list of items
# This is interesting because we get a tuple for each list
# item and each tuple has two parts which we can store in
# multiple variables in the loop.
for key, value in myDictionary.items():
    print(key, '->', value)


# While loops are similar to C/C++. 
x = 0
while x < 4:
    print("Not yet!")
    x += 1
print("Done!")


# You can also perform more standard index based looping
# using the len() function on an iterable type
index = 0
while index < len(myList):
    print(myList[index])
    index += 1
