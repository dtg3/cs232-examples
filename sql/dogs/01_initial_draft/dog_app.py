"""
This program allows for CRUD operations on the dog database.
NOTE: This docstring format will use reST documentation style.
"""

import os

from dotenv import load_dotenv

from dog_db import DogDB
from dog_db import Dog
from init_db import  setup_database 

load_dotenv()

def find_dogs(database):
    dog_name = input("Enter dog by name: ")
    result_set = database.get_dogs_by_name(dog_name)
    
    print(len(result_set), "record(s) found")
    for dog in result_set:
        print(">", dog)


def add_dog(database):
    dog_name = input("Enter the dog's name: ")
    dog_age = int(input("Enter the dog's age: "))
    dog_breed = input("Enter the dog's breed: ")

    database.add_dog(Dog(dog_name, dog_age, dog_breed))


def update_dog(database):
    old_dog_name = input("Enter the name of the dog to update: ")
    new_dog_name = input("Enter the updated dog name: ")
    new_dog_age = int(input("Enter the updated dog age: "))
    new_dog_breed = input("Enter the updated dog breed: ")

    updated_dogs = database.update_dog(
        old_dog_name, Dog(new_dog_name, new_dog_age, new_dog_breed)
    )

    for dog in updated_dogs:
        print(">", dog)


def remove_dog(database):
    dog_name = input("Enter the name of the dog to delete: ")
    database.delete_dog(dog_name)


def main():
    setup_database("dog_data.csv")
    database = DogDB(
        os.getenv("DBHOST"),
        os.getenv("DBUSERNAME"),
        os.getenv("DBPASSWORD"),
        os.getenv("DATABASE")
    )
    
    quit = False

    while (not quit):
        print("What operation would you like to perform?")
        print("1) Create a new dog record")
        print("2) Search for a dog record")
        print("3) Update an existing dog record")
        print("4) Delete a dog record")
        print("q) Quit")
        option = input("Please make your selection: ")
        
        if (option == "1"):
            add_dog(database)  
        elif (option == "2"):
            find_dogs(database)
        elif (option == "3"):
            update_dog(database)
        elif (option == "4"):
            remove_dog(database)
        else:
            quit = option.lower() == 'q'

        print('')

if __name__ == "__main__":
    main()

