# Local Modules
from creatures import Animal
from creatures import Dog

def main():
    my_chicken = Animal("Cluck")
    my_chicken.speak()

    my_dog = Dog()
    my_dog.speak()
    my_dog.roll_over()

    my_animals = [my_chicken, my_dog]

    for animal in my_animals:
        # Since only the dog only has the
        # roll_over() function we can only
        # use functions that both the base
        # and derived classes have
        animal.speak()


if __name__ == "__main__":
    main()
