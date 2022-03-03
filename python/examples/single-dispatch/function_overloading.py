from functools import singledispatch

from my_class import SimpleClass

# Singledispatch is a decorator that allows you to
# specify how a function should behave based on the
# types of the arguements supplied. This has a similar
# effect to overloading a function in C++, but the 
# mechanim is a bit like using Templates. Single
# dispatch ONLY CHECKS THE TYPE OF THE FIRST
# argument to the function.

# This decorator indicates that we intend to use
# this function with the single dispatch feature.
# If none of of the registered dispatches provided
# below match the type of the first argument, this
# function will be called.
@singledispatch
def add(a, b):
    raise NotImplementedError(f"Unsupported type: {type(a)}")

# Once you have defined a function that will be used
# by single dispatch, you can use the following decorator
# format to register a different behavior based on the type
# of the first argument only:
#   @[function_name].register([type])
#
# Note that the name of the function is represented in the
# decorator, and as such, we do not need to supply the actual
# name again. This underscore notation is used in the offical
# Python documentation.
#
# It is important to note that when using this decorator,
# you CANNOT use the same function name, which is why we
# simply use _
@add.register(int)
def _(a, b):
    """Dispatch function called when add() is passed
    an int as the first parameter
    """
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(str)
def _(a, b):
    """Dispatch function called when add() is passed
    a string as the first parameter
    """
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(list)
def _(a, b):
    """Dispatch function called when add() is passed
    a list as the first parameter
    """
    print("First argument is of type ", type(a))
    print(a + b)


# Is is even possible to register classes as
# types for the dispatch
@add.register(SimpleClass)
def _(a, b):
    """Dispatch function called when add() is passed
    a SimpleClass as the first parameter
    """
    a.simple_function()


def main():
    add(1, 2)
    add('Python', 'Programming')
    add([1, 2, 3], [5, 6, 7])
    add(SimpleClass(), 1)

    # Floats are not one of the types listed,
    # so this would call the first add function
    # that was defined as a single dispatch and
    # throw NotImplementedError. You can uncomment
    # and run the link below to verify...or trust me :)
    #add(1.4, 1.5)


if __name__ == '__main__':
    main()    