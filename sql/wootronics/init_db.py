"""
Database functionality to connect, initialize and insert data
into the wootronics database
"""

# Python library imports
import os
import csv
from datetime import datetime

# Third-party imports
import mysql.connector


def setup_database(csvfile):
    """
    Function to initialize the MySQL database

    :param csvfile: woo-tronics csv data
    """

    create_database()
    create_tables()
    populate_tables(csvfile)


def connect_db():
    """
    Connect to the MySQL database

    :return: Connection object to the MySQL database
    """

    conn = mysql.connector.connect(
        host=os.getenv("DBHOST"),
        user=os.getenv("DBUSERNAME"),
        password=os.getenv("DBPASSWORD"),
        database=os.getenv("DATABASE")
    )
    return conn


def create_database():
    """
    Create the MySQL database to store information for the wootronics store
    """

    conn = mysql.connector.connect(
        host=os.getenv("DBHOST"),
        user=os.getenv("DBUSERNAME"),
        password=os.getenv("DBPASSWORD")
    )

    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"DROP DATABASE IF EXISTS {os.getenv('DATABASE')};")
    cursor.execute(f"CREATE DATABASE {os.getenv('DATABASE')};")
    conn.close()


def create_tables():
    """
    Add the tables to the wootronics database in MySQL
    """

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    
    create_customers_table(cursor)
    create_companies_table(cursor)
    create_products_table(cursor)
    create_orders_table(cursor)
    create_ordered_products_table(cursor)

    cursor.close()
    conn.close()


def create_customers_table(cursor):
    """
    Establish the schema for the customers table

    :param cursor: cursor to run commands on the database
    """
    
    cursor.execute(
        ''' 
        CREATE TABLE customers
        (
            customer_id INT UNSIGNED,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email_address VARCHAR(100),
            CONSTRAINT pk_customer PRIMARY KEY (customer_id),
            CONSTRAINT unique_email UNIQUE (email_address)
        );
        '''
    )


def create_companies_table(cursor):
    """
    Establish the schema for the companies table

    :param cursor: cursor to run commands on the database
    """
    
    cursor.execute(
        ''' 
        CREATE TABLE companies
        (
            company_id INT UNSIGNED,
            name VARCHAR(150),
            phone_number VARCHAR(15),
            CONSTRAINT pk_company_id PRIMARY KEY (company_id),
            CONSTRAINT unique_company_phone_number UNIQUE (phone_number)
        );
        '''
    )


def create_products_table(cursor):
    """
    Establish the schema for the products table

    :param cursor: cursor to run commands on the database
    """

    cursor.execute(
        ''' 
        CREATE TABLE products
        (
            product_id INT UNSIGNED,
            name VARCHAR(150),
            price DOUBLE,
            company_id INT UNSIGNED,
            CONSTRAINT pk_product_id PRIMARY KEY (product_id),
            CONSTRAINT fk_company_id FOREIGN KEY (company_id)
                REFERENCES companies (company_id)
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        '''
    )


def create_orders_table(cursor):
    """
    Establish the schema for the orders table

    :param cursor: cursor to run commands on the database
    """

    cursor.execute(
        ''' 
        CREATE TABLE orders
        (
            order_id INT UNSIGNED,
            customer_id INT UNSIGNED,
            date DATE,
            CONSTRAINT pk_order_id PRIMARY KEY (order_id),
            CONSTRAINT fk_customer_id FOREIGN KEY (customer_id)
                REFERENCES customers (customer_id)
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        '''
    )


def create_ordered_products_table(cursor):
    """
    Establish the schema for the ordered_products table.
    
    This table will serve as the linking table for the many-to-many
    relationships between the orders and products tables.

    :param cursor: cursor to run commands on the database
    """

    cursor.execute(
        ''' 
        CREATE TABLE ordered_products
        (
            order_id INT UNSIGNED,
            product_id INT UNSIGNED,
            CONSTRAINT pk_ordered_products PRIMARY KEY (order_id, product_id),
            CONSTRAINT fk_product_id FOREIGN KEY (product_id)
                REFERENCES products (product_id)
                ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_order_id FOREIGN KEY (order_id)
                REFERENCES orders (order_id)
                ON DELETE RESTRICT ON UPDATE CASCADE
        );
        '''
    )


def populate_tables(csvfile):
    """
    Insert data for woo-tronics

    :param csvfile: woo-tronics csv data
    """
    
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    with open(csvfile, "r") as csv_input:
        reader = csv.DictReader(csv_input)
        for row in reader:
            insert_customer(cursor, row)
            insert_company(cursor, row)
            insert_product(cursor, row)
            insert_order(cursor, row)
            insert_ordered_product(cursor, row)
    
    conn.commit()
    cursor.close()
    conn.close()


def insert_customer(cursor, row_data):
    """
    Insert data from the CSV file into the customers table

    :param cursor: cursor to run commands on the database
    :param row_data: row of data from the CSV file to represent a record
    """

    sql_customer_insert = """
        INSERT IGNORE INTO customers (customer_id, first_name, last_name, email_address)
        VALUES (%s, %s, %s, %s);
    """

    insert_values = (
        int(row_data['customer_id']),
        row_data['first_name'],
        row_data['last_name'],
        row_data['customer_email']
    )
    cursor.execute(sql_customer_insert, insert_values)


def insert_company(cursor, row_data):
    """
    Insert data from the CSV file into the companies table

    :param cursor: cursor to run commands on the database
    :param row_data: row of data from the CSV file to represent a record
    """

    sql_company_insert = """
        INSERT IGNORE INTO companies (company_id, name, phone_number)
        VALUES (%s, %s, %s);
    """
    
    insert_values = (
        int(row_data['company_id']),
        row_data['company_name'],
        row_data['phone_number']
    )
    cursor.execute(sql_company_insert, insert_values)

def insert_product(cursor, row_data):
    """
    Insert data from the CSV file into the products table

    :param cursor: cursor to run commands on the database
    :param row_data: row of data from the CSV file to represent a record
    """

    sql_product_insert = """
        INSERT IGNORE INTO products (product_id, name, price, company_id)
        VALUES (%s, %s, %s, %s);
    """

    insert_values = (
        int(row_data['item_id']),
        row_data['item_name'],
        float(row_data['item_price_usd']),
        int(row_data['company_id'])
    )
    cursor.execute(sql_product_insert, insert_values)


def insert_order(cursor, row_data):
    """
    Insert data from the CSV file into the orders table

    :param cursor: cursor to run commands on the database
    :param row_data: row of data from the CSV file to represent a record
    """

    sql_order_insert = """
        INSERT IGNORE INTO orders (order_id, customer_id, date)
        VALUES (%s, %s, %s);
    """

    insert_values = (
        int(row_data['order_id']),
        int(row_data['customer_id']),
        datetime.strptime(row_data['order_date'], '%m-%d-%Y').date()
    )
    cursor.execute(sql_order_insert, insert_values)


def insert_ordered_product(cursor, row_data):
    """
    Insert data from the CSV file into the ordered_products table

    :param cursor: cursor to run commands on the database
    :param row_data: row of data from the CSV file to represent a record
    """
    sql_ordered_products_insert = """
        INSERT INTO ordered_products (order_id, product_id)
        VALUES (%s, %s);
    """
    
    insert_values = (
        int(row_data['order_id']),
        int(row_data['item_id'])
    )
    cursor.execute(sql_ordered_products_insert, insert_values)
