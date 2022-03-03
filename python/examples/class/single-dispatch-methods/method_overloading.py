from functools import singledispatchmethod

class Negator:
    """This works like single dispatch for functions,
    but has a different decorater that is specifically
    used for class methods. Once again, this only checks
    the first parameter AFTER the self argument as that
    will always be a reference to the class itself.
    
    It is important to note that when using this decorator,
    you CANNOT use the same function name, which is why we
    simply use _
    """

    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError(f"Cannot negate a {type(arg)}")


    @neg.register(int)
    def _(self, arg):
        return -arg


    @neg.register(bool)
    def _(self, arg):
        return not arg


def main():
    negator_object = Negator()

    print(negator_object.neg(10))
    print(negator_object.neg(True))
    
    # Error!
    #print(negator_object.neg("Hello"))

if __name__ == "__main__":
    main()