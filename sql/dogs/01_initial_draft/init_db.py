import os
import csv

import mysql.connector


def setup_database(csvfile):
    create_tables()
    populate_tables(csvfile)


def populate_tables(csvfile):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    sql_insert = "INSERT INTO dogs (name, age, breed) VALUES (%s, %s, %s)"
    with open(csvfile, "r") as csv_input:
        reader = csv.DictReader(csv_input)
        for row in reader:
            insert_values = (row['Name'], int(row['Age']), row['Breed'])
            cursor.execute(sql_insert, insert_values)
    
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
        CREATE TABLE dogs
        (
            name VARCHAR(50),
            age TINYINT UNSIGNED,
            breed VARCHAR(100)
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
   