"""Python Functions

Demonstrate the use of Python functions.
"""


# Functions have a different format than C/C++
# The def keyword indicates the intention to
# DEFINE a function. Functions can have zero
# or more parameters.
def display_greeting():
    """Prints a greeting to the console"""
    print("Hello")


# Function parameters don't need a type like in
# C/C++ as they are dynamically typed like all
# variabes in Python.
def display_greeting_with_name(name):
    """Prints a user specific greeting to the console
    
    Args:
        name (string): user name to be displayed with the greeting
    """
    print("Hello,", name)


# You can use named parameters to provide a default
# values and make the parameters self-documenting.
# Parameters without the name= notation are referred
# to as positional parameters. Named parameters MUST
# appear after all positional parameters.
def delimited_list(values, separator=','):
    """Creates a deliniated string make up of items in values 

    Args:
        values (list): List of values
        separator (str): The separator between items in value

    Returns:
        string: the delimited list of values
    """
    delimited_string = ""
    for value in values:
        # This string is called a format string (or f string
        # for short). This allows you to insert variables 
        # directly into a string. This syntax only works
        # in Python 3.6 or higher.
        delimited_string += f"{value}{separator}"
    
    return delimited_string


def main():
    """Starting function to run the 
    complete sample program
    """

    display_greeting()

    display_greeting_with_name("Sarah")
    print(delimited_list(["apple", "grape", "pear"]))

    # If there is a fixed number of positional arguments
    # then you can use the parameters in order with the
    # correct behavior.
    print(delimited_list([3, 2, 1], '...'))
    # If there is an arbitrary number of positional
    # arguments you need to refer to the named argument
    # by name. You can also use the name for self
    # documentation.
    print(delimited_list([3, 2, 1], separator='...'))


# This is a special condition that means when we execute
# this script as a standalone program rather than just
# call the functions from another script, the code
# in the conditional gets executed. For now, think of it
# like the int main() function in C/C++.
# We will see this more later...
if __name__ == "__main__":
    main()
