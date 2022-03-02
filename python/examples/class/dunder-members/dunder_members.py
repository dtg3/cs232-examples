# In this example we see a case where
# a member of a class is the same for
# both the base class and the derived
# class (__data) each with thier own
# purpose and value. Since a derived
# class gets access to all things in
# the base class, we need to avoid having
# data be overwritten for the data variable.
# When we say __data, name mangling takes
# place to append _ClassName to the variable:
#   _BaseClass__data    -> for base class
#   _DerivedClass__data -> for derived class
# This allows both variable names to be unique
# to the classes and avoid one overwriting the
# other.
# You can verify this by removing all of the 
# leading __ from the usage of data and the
# result will be 21 (DerivedClass value) for
# both function calls.
class BaseClass():
    def __init__(self):
        self.data = 42
    

    def base_show_data(self):
        print(self.__data)
    
class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.__data = 21


    def derived_show_data(self):
        print(self.__data)


def main():
    x = DerivedClass()
    x.base_show_data()
    x.derived_show_data()


if __name__ == "__main__":
    main()
    