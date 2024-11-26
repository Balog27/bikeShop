
import pyodbc

# Define connection parameters
server = 'DAVID_BALOG_LAP\SQLEXPRESS'       # e.g., 'localhost' or 'YOUR_SERVER_NAME'
database = 'BikeShopDB'   # Your database name in SSMS
username = 'Balog David'   # If using SQL Server Authentication
password = ''   # If using SQL Server Authentication

# Connection string
connection_string = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=DAVID_BALOG_LAP\SQLEXPRESS;'
    r'DATABASE=BikeShopDB;'  # Replace with your database name
    r'Trusted_Connection=yes;'  # Uses Windows Authentication
)

conn = pyodbc.connect(connection_string)
print("Connection Successful!")

# Example query (fetching data)
# ("Fetching data from the database")
cursor = conn.cursor()

################ prints tables in the database
cursor.execute("""
        SELECT TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_TYPE = 'BASE TABLE'
    """)

    # Fetch and print all table names
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])

###################### PRINT THE CONTENT OF THE TABLES

for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        print("-" * (len(table_name) + 8))  # Decorative line for better readability

        # Execute a query to select all rows from the current table
        cursor.execute(f"SELECT * FROM [{table_name}]")  # Brackets handle special characters in table names

        # Fetch column names for the table
        columns = [column[0] for column in cursor.description]
        print("\t".join(columns))  # Print column headers

        # Fetch all rows and print each one
        rows = cursor.fetchall()
        for row in rows:
            print("\t".join(str(item) if item is not None else 'NULL' for item in row))

print("DONE")
# Close the connection
conn.close()
