import psycopg2


# Connect to your PostgreSQL database
""""conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="123456"
)

conn.autocommit = True
cursor = conn.cursor()
print("DB Connection reached")

# Check if the cursor is closed
if cursor.closed:
    print("Cursor is closed !!!.")
else:
    print("Cursor is open.")
    
sql = ''' CREATE database test ''';
# executing above query
cursor.execute(sql)
print("Database has been created successfully !!");
cursor.close()
conn.close()"""
# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    dbname="test",
    user="postgres",
    password="123456"
)

conn.autocommit = True
cursor = conn.cursor()
print("DB Connection reached")

# Check if the cursor is closed
if cursor.closed:
    print("Cursor is closed !!!.")
else:
    print("Cursor is open.")
# Open and read the .sql file
with open('e://mydb//Dataset//Chinook_PostgreSql.sql', 'r') as file:
    sql = file.read()
    
# Execute the SQL commands
cursor.execute(sql)

# Commit the transaction
conn.commit()

#Display all the tables
query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    AND table_type = 'BASE TABLE';
"""

# Execute the query
cursor.execute(query)

# Fetch all results
tables = cursor.fetchall()

# Print the table names
print("Tables in the database:")
for table in tables:
    print(table[0])
