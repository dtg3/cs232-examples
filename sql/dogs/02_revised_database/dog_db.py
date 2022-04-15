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

    def __init__(self, name, age, breed, id=None):
        """
        Initialize a Dog object using its name, age, and breed.

        :param name: name of the dog
        :param age: age of the dog
        :param breed: breed of the dog
        """
        self._name = name
        self._age = age
        self._breed = breed
        self._id = id


    def __repr__(self):
        """
        Create a string representation of a dog.

        The format is as follows:

           <name>, a <age> year old <breed>

        :return: the string representation of the dog
        """
        dog_details = f"{self._name}, a {self._age} year old {self._breed}"
        if self._id:
            dog_details = f"[id: {self._id}] " + dog_details
        return dog_details


    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def breed(self):
        return self._breed
    
    @property
    def id(self):
        return self._id

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


    def get_breed(self, breed_name):
        query_breed = 'SELECT * FROM breeds WHERE name=%s;'
        
        cur = self._conn.cursor(dictionary=True)
        cur.execute(query_breed, (breed_name,))
        breed_record = cur.fetchone()
        
        cur.close()
        return breed_record
    

    def insert_breed(self, breed_name):
        query_breed_insert = '''
            INSERT INTO breeds (name) VALUES (%s);
        '''
        cur = self._conn.cursor(dictionary=True)
        cur.execute(query_breed_insert, (breed_name,))
        self._conn.commit()

        cur.execute("SELECT LAST_INSERT_ID() id")
        breed_id = cur.fetchone()


        cur.close()
        return breed_id


    def add_dog(self, dog):
        """
        Add a new dog record to the database

        :param dog: new dog to be added to the database
        """

        breed = self.get_breed(dog.breed)
        if not breed:
            breed = self.insert_breed(dog.breed)

        insert_dog_query = '''
            INSERT INTO dogs (name, age, breed_id)
            VALUES (%s, %s, %s);
        '''

        cur = self._conn.cursor()
        cur.execute(insert_dog_query, (dog.name, dog.age, breed["id"]))
        self._conn.commit()

        print(cur.rowcount, "record(s) affected")
        
        cur.execute("SELECT LAST_INSERT_ID() id")
        new_dog_id = cur.fetchone()
        
        cur.close()
        return new_dog_id

    
    def delete_dog(self, id):
        """
        Remove a dog record from the database

        :param name: name of the dog to be removed from the database
        """
        query = 'DELETE FROM dogs WHERE id=%s;'

        cur = self._conn.cursor()
        cur.execute(query, (id,))
        self._conn.commit()

        print(cur.rowcount, "record(s) affected")
        cur.close()


    def update_dog(self, id, new_dog):
        """
        Update a dog's record in the database using the name

        :param dog: new dog to be added to the database
        """

        breed = self.get_breed(new_dog.breed)
        if not breed:
            breed = self.insert_breed(new_dog.breed)

        query = '''
            UPDATE dogs SET name=%s, age=%s, breed_id=%s
            WHERE id=%s;
        '''

        cur = self._conn.cursor()
        cur.execute(query, (new_dog.name, new_dog.age, breed["id"], id))
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
            SELECT d.name, d.age, b.name, d.id
            FROM dogs d
                INNER JOIN breeds b
                ON d.breed_id = b.id
            WHERE d.name = %s
        '''

        cur = self._conn.cursor()
        cur.execute(query, (name,))

        dogs = []

        for row in cur.fetchall():
            dog = Dog(row[0], row[1], row[2], row[3])
            dogs.append(dog)

        cur.close()
        return dogs


    def disconnect(self):
        self._conn.close()
