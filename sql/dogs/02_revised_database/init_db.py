import os
import csv

import mysql.connector


def setup_database(csvfile):
    create_tables()
    populate_tables(csvfile)


def populate_tables(csvfile):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    
    sql_dogs_insert = "INSERT INTO dogs (name, age, breed_id) VALUES (%s, %s, %s)"
    sql_breeds_find = "SELECT id FROM breeds WHERE name=(%s)"
    sql_breeds_insert = "INSERT INTO breeds (name) VALUES (%s)"

    with open(csvfile, "r") as csv_input:
        reader = csv.DictReader(csv_input)
        for row in reader:
            cursor.execute(sql_breeds_find, (row['Breed'],))
            breed_id = cursor.fetchone()
            if not breed_id:
                cursor.execute(sql_breeds_insert, (row['Breed'],))
                cursor.execute("SELECT LAST_INSERT_ID() id")
                breed_id = cursor.fetchone()
            
            cursor.execute(sql_dogs_insert, (row["Name"], row["Age"], breed_id["id"]))

    conn.commit()
    cursor.close()
    conn.close()


def create_tables():
    conn = mysql.connector.connect(
        host=os.getenv("DBHOST"),
        user=os.getenv("DBUSERNAME"),
        password=os.getenv("DBPASSWORD")
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"DROP DATABASE IF EXISTS {os.getenv('DATABASE')};")
    cursor.execute(f"CREATE DATABASE {os.getenv('DATABASE')};")
    cursor.execute(f"use {os.getenv('DATABASE')};")
    
    cursor.execute(
        ''' 
        CREATE TABLE breeds
        (
            id SMALLINT UNSIGNED AUTO_INCREMENT,
            name VARCHAR(100),
            CONSTRAINT pk_breed PRIMARY KEY (id),
            CONSTRAINT unique_breed_name UNIQUE (name)
        );
        '''
    )

    cursor.execute(
        ''' 
        CREATE TABLE dogs
        (
            id MEDIUMINT UNSIGNED AUTO_INCREMENT,
            name VARCHAR(50),
            age TINYINT UNSIGNED,
            breed_id SMALLINT UNSIGNED,
            CONSTRAINT pk_dogs PRIMARY KEY (id),
            CONSTRAINT fk_breed_id FOREIGN KEY (breed_id)
                REFERENCES breeds (id)
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        '''
    )

    cursor.close()
    conn.close()


def connect_db():
    conn = mysql.connector.connect(
        host=os.getenv("DBHOST"),
        user=os.getenv("DBUSERNAME"),
        password=os.getenv("DBPASSWORD"),
        database=os.getenv("DATABASE")
    )
    return conn
    