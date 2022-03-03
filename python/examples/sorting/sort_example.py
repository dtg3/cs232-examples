
# List to be sorted
my_list = [1, 3, 6, 8, 10, 2, 4, 5]

# Lists have a built in sort function with
# the default order being ascending
print("Using list's sort function")
my_list.sort()
# NOTE: sort modifies the original list
print(my_list)

# We can reverse this with the named
# parameter reverse and set it to True
my_list.sort(reverse=True)
print(my_list)

# For containers that don't have a sort function,
# python supplies a sorted function to help. This
# does not modify the original container, but instead
# returns a NEW container. Note that the first parameter
# of the function is the container you want to sort.
print(sorted(my_list))
# This also provides the reverse named parameter
print(sorted(my_list, reverse=True))

# The sorted function provides some more interesting behavior with
# more complex containers
dictionary = {"a" : 10, "c" : 50, "b" : 2}

# Recall that using the items() function on the dictionary provides
# an iterable dictionary item container with tuples of key value pairs. This
# is why it says dict_items before it prints them.
print("Display items in a dictionary:")
print(dictionary.items())

# What if we wanted to sort the items by the keys...or values?
# Both list's sort() AND the sorted() function allow for you to provide
# a function to help determining what values to use for sorting the container.
# Yes, you can pass functions as parameters to functions!
#
# Lets make a simple function first. It will expect a tuple and simply
# return the first item
def sort_by_dict_keys(tuple):
    return tuple[0]

# In the example below, the sorted function iterates over all the tuples in the
# dict_items container and passes each item to the sort_by_dict_keys()
# function we created above. Since this function returns tuple[0], the
# first element in the tuple, we sort by keys. If we returned tuple[1],
# the second element it would sort by value. Go ahead...try it!
print("Sorting the items in a dictionary by Keys")
print(sorted(dictionary.items(), key=sort_by_dict_keys))

# Now it's a little awkward to have to create a new function each time
# we may want to sort these more complicated structures in a different
# way. Python provides a way to call an anonymous (unnamed) function
# which is called a lambda function. Let's try the same thing again.
print("Sorting the items in a dictionary by Values")
print(sorted(dictionary.items(), key=lambda tuple: tuple[1]))

# Let's talk about what we just did there. We know that key takes a function
# to help identify what value in the tuple to use for sorting. We can think of
# the lambda keyword as the name of the function, and tuple as the parameter
# that will go to the function. The colon starts the statement that will be
# executed when the function is called and represents the value returned from
# our lambda function. If we were to write this in the usualy way it would look
# like this:
# def lambda(tuple):
#   return tuple[1]
#
# Looks familiar doesn't it?

# So this means that if we have complicated containers like lists of dictionaries or
# list of tuples, we can used the key parameter of the sort or sorted function to
# sort the elements in unique ways.
list_of_dictionaries = [ {"a" : 10, "b" : 1, "c" : 50}, {"a" : 44, "b" : 67, "c" : 22},
                         {"a" : 20, "b" : 170, "c" : 78}, {"a" : 2, "b" : 8, "c" : 30}]

# Sort by the value located at key "b" in the list of dictionaries
# Note that the variable in the lambda function (x in this case),
# can be named anything.
print("Sort Lists of Dictionaries")
print(sorted(list_of_dictionaries, key=lambda x: x["b"]))
# Sort by the value located at key "a" in the list of dictionaries
print(sorted(list_of_dictionaries, key=lambda x: x["a"]))

# Let's try it again using lists of tuples
list_of_tuples = [(1, "a", 5), (2, "w", 8), (11, "are", 30), (0, "hello", 6)]

# Sort the list of tuples using the values located at indices
# 0, 1, and 2 respectively.
print("Sorting Lists of Tuples")
print(sorted(list_of_tuples, key=lambda x: x[0]))
print(sorted(list_of_tuples, key=lambda x: x[1]))
print(sorted(list_of_tuples, key=lambda x: x[2]))

# Don't for get that you can also combine the key and reverse parameters
# to sort ascending or decending.
print("Sort the list of tuples in reverse order")
print(sorted(list_of_tuples, key=lambda x: x[2], reverse=True))
