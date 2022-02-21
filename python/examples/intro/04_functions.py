"""Python Functions

Demonstrate the use of Python functions.
"""

# Functions have a different format than C/C++
# The def keyword indicates the intention to
# DEFINE a function. Functions can have zero
# or more parameters.
from os import sep


def displayGreeting():
    """
    Prints a greeting to the console
    """
    print("Hello")


# Function parameters don't need a type like in
# C/C++ as they are dynamically typed like all
# variabes in Python.
def displayGreetingWithName(name):
    """
    Prints a user specific greeting to the console
    
    Args:
        name (string): user name to be displayed with the greeting
    """
    print("Hello,", name)


# You can use named parameters to provide a default
# values and make the parameters self-documenting.
# Parameters without the name= notation are referred
# to as positional parameters. Named parameters MUST
# appear after all positional parameters.
def delimitedList(values, separator=','):
    """
    Creates a deliniated string make up of items in values 

    Args:
        values (list): List of values
        separator (str): The separator between items in value

    Returns:
        string: the delimited list of values
    """
    delimitedString = ""
    for value in values:
        delimitedString += f"{value}{separator}"
    
    return delimitedString

# This is a special condition that means when we execute
# this script as a standalone program rather than just
# call the functions from another script, the code
# in the conditional gets executed. For now, think of it
# like the int main() function in C/C++.
# We will see this more later...
if __name__ == "__main__":
    displayGreeting()

    displayGreetingWithName("Sarah")
    print(delimitedList(["apple", "grape", "pear"]))

    # If there is a fixed number of positional arguments
    # then you can use the parameters in order with the
    # correct behavior.
    print(delimitedList([3, 2, 1], '...'))
    # If there is an arbitrary number of positional
    # arguments you need to refer to the named argument
    # by name. You can also use the name for self
    # documentation.
    print(delimitedList([3, 2, 1], separator='...'))

