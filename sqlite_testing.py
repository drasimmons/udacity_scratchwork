import sqlite3
from sqlite3 import Error

# Function to create sqlite connection object
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successfully initialized!")
    except Error as e:
        print(f"The error '{e}' occurred :()")

    return connection

# Create connection
sqliteConnection = create_connection('/Users/ambersimmons/Documents/Repositories/udacity_scratchwork/db/test_db.db')

# Create cursor object
cursor = sqliteConnection.cursor()

# Create some test table in the db
# Drop the GEEK table if already exists.
cursor.execute("DROP TABLE IF EXISTS geek")

# Creating table
# Table query
table = """ CREATE TABLE geek (
			Name VARCHAR(255) NOT NULL,
			GradeLevel CHAR(25) NOT NULL,
			ClassGrade CHAR(25),
			TestScore INT
		); """

# Execute cursor
cursor.execute(table)

print("Geek table was created.")

# Insert data into table
cursor.execute('''INSERT INTO geek VALUES ('Raju', '7th', 'A', 100)''') 
cursor.execute('''INSERT INTO geek VALUES ('Shyam', '8th', 'B', 86)''') 
cursor.execute('''INSERT INTO geek VALUES ('Baburao', '9th', 'C', 82)''') 

print("Data inserted into the table: \n") 

# Query table and
# Display data inserted 
data = cursor.execute('''SELECT * FROM geek''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
sqliteConnection.commit() 

print('\nChanges to db were committed.')

# Close the connection
if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed.')