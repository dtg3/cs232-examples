# To run this example, you will want to activate a virtual environment.
# If you do not know how to make a virtual environment in this directory
# be sure to read over the web-scraper.py documentation.
# 
# tldr;
# Setup Virtual Environment
#   On macOS: python3 -m venv env
#   On Windows: python -m venv env
# Activate the Virtual Environment
#   On Mac: source env/bin/activate
#   On Windows: env\Scripts\activate
#
# Once Virtual Environment is active
#   pip install python-dotenv
#   pip install mysql-connector-python
import os

from dotenv import load_dotenv
import mysql.connector

# Load environment data from the .secrets file.
# When you are developing, do NOT add this file
# to a GitHub repository (add this file to your
# .gitignore). I've added it to this repo as an
# example.
load_dotenv(".secrets")

# We can access the data from the file
# using the name of each variable in the
# .secrets file using the Python OS library.
mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_host = os.getenv("MYSQL_HOST")
mysql_database = os.getenv("MYSQL_DATABASE")


mydb = mysql.connector.connect(
  host = mysql_host,
  user = mysql_user,
  password = mysql_password
)

print(mysql_database)
mycursor = mydb.cursor()
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {mysql_database}")
mycursor.execute(f"USE {mysql_database}")

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


mycursor.execute(
    "INSERT INTO customers (name, address) VALUES (%s, %s)",
    ("Woo", "Beal"))
mydb.commit()

print(f"Inserted {mycursor.rowcount} records.") 
