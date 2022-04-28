"""
Supporting functions for initializing and loading the database
with data from the vgsales csv file.
"""
# Python library imports
import csv
import sys
import os

# Thrid-party imports
import mysql.connector

# Constant to represent the number of rows in the csv datafile
#   Used for the progress bar code
CSV_RECORD_COUNT = 16598


# I did not write this function, but found a simply GitHub gist online
#   with this functionality.
#   Code from: https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def initialize_database(csv_filename, force=False):
    """
    Primary function to bootstrap the initialization of the database,
    tables, and importing csv data.

    :param csv_filename: file name of the input csv file for data import
    :param force: overrides the database check and recreates the database
        when set to True
    """
    mydb = mysql.connector.connect(
        host=os.getenv("DBHOST"),
        user=os.getenv("DBUSERNAME"),
        password=os.getenv("DBPASSWORD")
    )

    mycursor = mydb.cursor(dictionary=True)

    # This code will query MySQL to see if the database exists.
    #   If the database already exits, we abort the initialization process.
    mycursor.execute(f"SHOW DATABASES LIKE '{os.getenv('DATABASE')}';")
    if not mycursor.fetchone() or force:
        mycursor.execute(f"DROP DATABASE IF EXISTS {os.getenv('DATABASE')};") 
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DATABASE')};")
        mycursor.execute(f"USE {os.getenv('DATABASE')}")

        create_tables(mycursor)
        populate_tables(mycursor, csv_filename)
        mydb.commit()
    
    mycursor.close()
    mydb.close()
    

def create_tables(mycursor):
    """
    Creates all the table schemas for the database

    :param mycursor: cursor to execute commands to MySQL
    """
    mycursor.execute(
        """
        CREATE TABLE genre
        (
            genre_id SMALLINT UNSIGNED AUTO_INCREMENT,
            genre_name VARCHAR(20),
            CONSTRAINT pk_genre PRIMARY KEY (genre_id, genre_name)
        );
        """
    )

    mycursor.execute(
        """
        CREATE TABLE publisher
        (
            publisher_id SMALLINT UNSIGNED AUTO_INCREMENT,
            publisher_name VARCHAR(50),
            CONSTRAINT pk_publisher PRIMARY KEY (publisher_id, publisher_name)
        );
        """
    )

    mycursor.execute(
        """
        CREATE TABLE platform
        (
            platform_id SMALLINT UNSIGNED AUTO_INCREMENT,
            platform_name VARCHAR(20),
            CONSTRAINT pk_platform PRIMARY KEY (platform_id , platform_name)
        );
        """
    )

    mycursor.execute(
        """
        CREATE TABLE game
        (
            game_id SMALLINT UNSIGNED AUTO_INCREMENT,
            game_name VARCHAR(200),
            platform_id SMALLINT UNSIGNED,
            publisher_id SMALLINT UNSIGNED,
            genre_id SMALLINT UNSIGNED,
            release_year YEAR,
            CONSTRAINT pk_game PRIMARY KEY (game_id, platform_id, publisher_id),
            CONSTRAINT fk_game_platform FOREIGN KEY (platform_id)
                REFERENCES platform (platform_id)
                ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_game_publisher FOREIGN KEY (publisher_id)
                REFERENCES publisher (publisher_id)
                ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_game_genre FOREIGN KEY (genre_id)
                REFERENCES genre (genre_id)
                ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """
    )

    mycursor.execute(
        """
        CREATE TABLE game_sales
        (
            sales_id SMALLINT UNSIGNED AUTO_INCREMENT,
            game_id SMALLINT UNSIGNED,
            na_sales FLOAT UNSIGNED,
            eu_sales FLOAT UNSIGNED,
            jp_sales FLOAT UNSIGNED,
            other_sales FLOAT UNSIGNED,
            global_sales FLOAT UNSIGNED,
            CONSTRAINT pk_sales PRIMARY KEY (sales_id, game_id),
            CONSTRAINT fk_game_sale_id FOREIGN KEY (game_id)
                REFERENCES game (game_id)
                ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """
    )


def populate_tables(mycursor, csv_filename):
    """
    Populate tables initializes all the database tables
    with data from the CSV file.

    :param mycursor: MySQL cursor to run commands 
    :param csv_filename: name of the csv file to open and read
    """
    publisher_names = set()
    genre_names = set()
    platform_names = set()

    with open(csv_filename, 'r') as csv_data:
        reader = csv.DictReader(csv_data)
        
        count = 0
        print("IMPORTING DATA")
        for item in reader:
            count += 1
            progress(count, CSV_RECORD_COUNT)
            database_ids = {}
            database_ids.update(insert_publisher(mycursor, publisher_names, item))
            database_ids.update(insert_genre(mycursor, genre_names, item))
            database_ids.update(insert_platform(mycursor, platform_names, item))
            database_ids.update(insert_game(mycursor, database_ids, item))
            insert_game_sale(mycursor, database_ids, item)
    
    # Move to line after progress bar
    print()
    

def insert_publisher(mycursor, known_publishers, record):
    """
    Insert game publisher data into the appropriate table

    :param mycursor: MySQL cursor to run commands 
    :param known_publishers: set to see if a publisher has already been added to the database
    :param record: the raw record of data from the CSV file
    """
    if record["Publisher"] not in known_publishers:
        insert_publisher_statment = """
            INSERT INTO publisher
                (publisher_id, publisher_name)
            VALUES
                (null, %s);
            """
        mycursor.execute(insert_publisher_statment, (record["Publisher"],))
        mycursor.execute("SELECT LAST_INSERT_ID() publisher_id")
        known_publishers.add(record["Publisher"])
    else:
        select_publisher_statement = """
            SELECT publisher_id FROM publisher
            WHERE publisher_name = %s;
        """
        mycursor.execute(select_publisher_statement, (record["Publisher"],))
    return mycursor.fetchone()


def insert_genre(mycursor, known_genres, record):
    """
    Insert game genre data into the appropriate table

    :param mycursor: MySQL cursor to run commands 
    :param known_genres: set to see if a genre has already been added to the database
    :param record: the raw record of data from the CSV file
    """
    if record["Genre"] not in known_genres:
        insert_genre_statement = """
            INSERT INTO genre
                (genre_id, genre_name)
            VALUES
                (null, %s);
        """
        mycursor.execute(insert_genre_statement, (record["Genre"],))
        mycursor.execute("SELECT LAST_INSERT_ID() genre_id")
        known_genres.add(record["Publisher"])
    else:
        select_genre_statement = """
            SELECT genre_id FROM genre
            WHERE genre_name = %s;
        """
        mycursor.execute(select_genre_statement, (record["Genre"],))
    return mycursor.fetchone()


def insert_platform(mycursor, known_platforms, record):
    """
    Insert game platform data into the appropriate table

    :param mycursor: MySQL cursor to run commands 
    :param known_platforms: set to see if a platform has already been added to the database
    :param record: the raw record of data from the CSV file
    """
    if record["Platform"] not in known_platforms:
        insert_platform_statement = """
            INSERT INTO platform
                (platform_id, platform_name)
            VALUES
                (null, %s);
        """
        mycursor.execute(insert_platform_statement, (record["Platform"],))
        mycursor.execute("SELECT LAST_INSERT_ID() platform_id")
        known_platforms.add(record["Platform"])
    else:
        select_platform_statement = """
            SELECT platform_id FROM platform
            WHERE platform_name = %s;
        """
        mycursor.execute(select_platform_statement, (record["Platform"],))
    return mycursor.fetchone()


def insert_game(mycursor, database_ids, record):
    """
    Insert game data into the appropriate table

    :param mycursor: MySQL cursor to run commands 
    :param database_ids: dictionary of id values of primary keys from other tables
        to be used as foreign keys in the inserted record
    :param record: the raw record of data from the CSV file
    """
    insert_game_statement = """
        INSERT INTO game
            (game_id, game_name, platform_id, publisher_id, genre_id, release_year)
        VALUES
            (null, %s, %s, %s, %s, %s);
    """
    values = (record["Name"], database_ids["platform_id"], database_ids["publisher_id"],
                database_ids["genre_id"], int(record["Year"]) if record["Year"] != "N/A" else None)
    mycursor.execute(insert_game_statement, values)
    mycursor.execute("SELECT LAST_INSERT_ID() game_id")
    return mycursor.fetchone()


def insert_game_sale(mycursor, database_ids, record):
    """
    Insert sales data into the appropriate table

    :param mycursor: MySQL cursor to run commands 
    :param database_ids: dictionary of id values of primary keys from other tables
        to be used as foreign keys in the inserted record
    :param record: the raw record of data from the CSV file
    """
    insert_game_sale_statement = """
        INSERT INTO game_sales
            (sales_id, game_id, na_sales, eu_sales, jp_sales, other_sales, global_sales)
        VALUES
            (null, %s, %s, %s, %s, %s, %s);
    """
    values = (
        database_ids["game_id"], 
        float(record["NA_Sales"]) if record["NA_Sales"] != "N/A" else "null",
        float(record["EU_Sales"]) if record["EU_Sales"] != "N/A" else "null",
        float(record["JP_Sales"]) if record["JP_Sales"] != "N/A" else "null",
        float(record["Other_Sales"]) if record["Other_Sales"] != "N/A" else "null",
        float(record["Global_Sales"]) if record["Global_Sales"] != "N/A" else "null"
    )
    mycursor.execute(insert_game_sale_statement, values)
