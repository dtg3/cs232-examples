# Example code using the @property decorator

# This module just allows us to "hash"
# the password string
import hashlib

class User:
    def __init__(self, name, password):
        self._name = name
        self._password = password


    # This automatically sets up the
    # property to have "getter" or
    # read access to our (technically)
    # private variable _name.
    @property
    def name(self):
        print('Getting name')
        return self._name


    # Any time you use assignment on the
    # name property, this function is called
    # giving you "setter" or mutating access
    # to _name.
    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value


    # A bit like a destructor if you needed
    # to perform additional actions before
    # destroying an object with del.
    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name


    # This is a good use case for the property
    # as the method of retrieving the password
    # do not reveal the content. This means that
    # when people use the property to access this
    # variable they are being supplied the data
    # in its intended format
    #
    # You also don't have to supply certain property
    # types for all of the variables. In this case, we
    # can get the password, but cannot set it
    # using the property.
    #
    # Disclaimer: This is not how we secure passwords
    # as the content still exists in plain text form
    # in the _password data member above. This is only
    # a demonstration.
    @property
    def password(self):
        hash = hashlib.sha256(self._password.encode())
        return hash.hexdigest()


def main():
    p = User('Adam', "secret")
    print(f"Name: {p.name}")
    print(f"Password: {p.password}")

    # Trying to change the password will cause
    # an error. But since the _password is still
    # technically public, this just defines that
    # the interface in not meant to allow this
    # action.
    #p.password = "new secret"

    p.name = 'John'
    del p.name


if __name__ == "__main__":
    main()
