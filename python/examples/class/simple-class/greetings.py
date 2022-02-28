class Greeting:
    """A class to greet people in unique ways

    Note that all class functions require at least
    one parameter. By convention this is named self.
    This allows the functions to refer to the specific
    instance of the class calling them.

    Attributes:
        name (string): name of the person to greet
    """

    # Python does NOT (natively) support overloading
    # of methods. For example, we cannot have
    # an init for multiple cases:
    #   __init__(self)       -> No arguments
    #   __init__(self, name) -> Provide a name
    # Even if the number of arguments differs
    # a function name must be unique in its
    # scope. In this example, we make the name
    # argument optional with a named parameter and
    # a default value to simulate calls like
    # this:
    #   Greeting()        -> No arguments
    #   Greeting("Sally") -> One argument
    def __init__(self, name = ''):
        """Initialize the Greeting instance
        
        Note that this is similar to a constructor in
        C++, but not exactly the same. The greeting
        object already exists by the time we reach this
        function. In C++, the constructor creates AND
        initializes the object instance. There is a
        built in function for classes called __new__
        that deals with object creation before the
        initialization with __init__. For this class,
        you will not need to worry about making a
        function for __new__.

        Args:
            name (str): optional name of the person to be
                greeted
        """
        self.name = name

    # A function or data member with a leading single
    # underscore (_) is indicated as private. This is
    # NOT enforced by the Python interpreter, but is
    # instead an agreed convention. This is NOT the
    # same as leading double underscore (__) which
    # is NOT used to make things private, but instead
    # performs "name mangling" to avoid instances where
    # naming conflicts might occur (usually resulting 
    # from inheritance). See dunder-members example for
    # __ usage.
    def _build_greeting(self):
        """Private function to help construct the greeting"""
        greeting = "Hello!"
        if self.name:
            greeting = f"{greeting[:-1]}, {self.name}!"    
        return greeting


    def greet(self, shout = False):
        """A function designed to say hello to a user
        Args:
            shout (boolean): decide whether string should
                be presented in upper case
        """
        greeting = self._build_greeting()

        if shout:
            print(greeting.upper())
        else:
            print(greeting)


def main():
    greeter = Greeting()
    greeter = Greeting("bob")
    greeter.greet()
    greeter.greet(True)  # shouting!


if __name__ == "__main__":
    main()