"""Example of Inheritance

Animal is our base class, and
the Dog is the derived class
that is based on the Animal
class.
"""


class Animal:
    """Animal class to demonstrate simple class creation

    Animal will also serve as the base class for 
    the Dog derived class (sub class).

    Attributes:
        sound (str): the noise an animal makes
    """


    def __init__(self, sound):
        """Initialization method for the Animal class
        
        Args:
            sound (str): the noice an animal should make
        """
        self.sound = sound
    

    def speak(self):
        """Output the sound that the animal makes"""
        print(f"Animal says: {self.sound}")


class Dog(Animal):
    """Animal class to demonstrate simple class creation

    Animal will also serve as the base class for 
    the Dog derived class (sub class).
    """


    def __init__(self):
        """Initialization method for the Dog class
        
        A parameter is not needed as the Dog class
        knows what sound the animal should make and
        utilizes the super() function to pass that
        to the Animal base class initializer function
        """
        super().__init__("Woof")


    def speak(self):
        """Output the sound that a Dog makes"""
        print(f"Dog says: {self.sound}")
    

    def roll_over(self):
        """Action exclusive to the Dog class"""
        print("Dog rolls over")
