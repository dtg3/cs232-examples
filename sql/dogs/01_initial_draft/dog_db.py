"""
This module provides functionality for interacting with a database of dogs.
NOTE: This docstring format will use reST documentation style.
"""

import mysql.connector


class Dog:
    """
    An object from this class represents a dog. In particular it stores the
    name, age, and breed.
    """

    def __init__(self, name, age, breed):
        """
        Initialize a Dog object using its name, age, and breed.

        :param name: name of the dog
        :param age: age of the dog
        :param breed: breed of the dog
        """
        self._name = name
        self._age = age
        self._breed = breed


    def __repr__(self):
        """
        Create a string representation of a dog.

        The format is as follows:

           <name>, a <age> year old <breed>

        :return: the string representation of the dog
        """
        return '{}, a {} year old {}'.format(self._name, self._age,
                                             self._breed)


    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def breed(self):
        return self._breed

    def increment_age(self):
        self._age += 1


class DogDB:
    """
    This class provides an interface for interacting with a database of dogs.
    """

    def __init__(self, host, username, password, database):
        self._conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )


    def add_dog(self, dog):
        """
        Add a new dog record to the database

        :param dog: new dog to be added to the database
        """
        query = '''
            INSERT INTO dogs (name, age, breed)
            VALUES (%s, %s, %s);
        '''

        cur = self._conn.cursor()
        cur.execute(query, (dog.name, dog.age, dog.breed))
        self._conn.commit()

        print(cur.rowcount, "record(s) affected")
        cur.close()
    

    def delete_dog(self, name):
        """
        Remove a dog record from the database

        :param name: name of the dog to be removed from the database
        """
        query = 'DELETE FROM dogs WHERE name=%s;'

        cur = self._conn.cursor()
        cur.execute(query, (name,))
        self._conn.commit()

        print(cur.rowcount, "record(s) affected")
        cur.close()
        

    def update_dog(self, dog_name, new_dog):
        """
        Update a dog's record in the database using the name

        :param dog: new dog to be added to the database
        """
        query = '''
            UPDATE dogs SET name=%s, age=%s, breed=%s
            WHERE name=%s;
        '''

        cur = self._conn.cursor()
        cur.execute(query, (new_dog.name, new_dog.age, new_dog.breed, dog_name))
        self._conn.commit()
        
        print(cur.rowcount, "record(s) affected")
        cur.close()
        
        return self.get_dogs_by_name(new_dog.name)


    def get_dogs_by_name(self, name):
        """
        Find a dog's record in the database using the name

        :param name: name of the dog
        :return: list of all dogs with a matching name
        """

        query = '''
            SELECT name, age, breed
            FROM dogs
            WHERE name = %s
        '''

        cur = self._conn.cursor()
        cur.execute(query, (name,))

        dogs = []

        for row in cur.fetchall():
            dog = Dog(row[0], row[1], row[2])
            dogs.append(dog)

        cur.close()
        return dogs


    def disconnect(self):
        self._conn.close()
