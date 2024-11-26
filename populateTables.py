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

try:
    # Connect to the database
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Enable IDENTITY_INSERT for Users table
    cursor.execute("SET IDENTITY_INSERT Users ON")

    # Insert data into Users table
    cursor.executemany(
        """
        INSERT INTO Users (UserID, Username, PasswordHash, Email, FirstName, LastName, PhoneNumber)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (1, 'admin', 'parola', 'Admin@gmail.com', 'Admin', 'Admin', '0722222222'),
            (2, "david", 'parola', 'david27balogg@yahoo.com', 'David', 'Balog', '0755555555'),
            (3, "ion", 'parola', 'ion@yahoo.com', 'Ion', 'Popescu', '0777777777'),
            (4, "maria", 'parola', 'maria@yahoo.com', 'Maria', 'Popescu', '0766666666'),
        ]
    )

    # Disable IDENTITY_INSERT for Users table
    cursor.execute("SET IDENTITY_INSERT Users OFF")

    # Enable IDENTITY_INSERT for BikeShops table
    cursor.execute("SET IDENTITY_INSERT BikeShops ON")

    # Insert data into BikeShops table
    cursor.executemany(
        """
        INSERT INTO BikeShops (ShopID, ShopName, Location, PhoneNumber, OwnerID)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (1, 'David Bike Shop', 'Cluj-Napoca', '0755555555', 1),
        ]
    )

    # Disable IDENTITY_INSERT for BikeShops table
    cursor.execute("SET IDENTITY_INSERT BikeShops OFF")

    # Enable IDENTITY_INSERT for Bikes table
    cursor.execute("SET IDENTITY_INSERT Bikes ON")

    # Insert data into Bikes table
    cursor.executemany(
        """
        INSERT INTO Bikes (BikeID, ShopID, Model, Brand, Type, Price, StockQuantity)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (1, 1, 'Mountain Bike', 'Trek', 'Mountain', 1000, 2),
            (2, 1, 'Road Bike', 'Specialized', 'Road', 1500, 5),
            (3, 1, 'City Bike', 'Giant', 'City', 800, 3),
            (4, 1, 'Suzuki SV650', 'Suzuki', 'Naked', 5000, 1),
        ]
    )

    # Disable IDENTITY_INSERT for Bikes table
    cursor.execute("SET IDENTITY_INSERT Bikes OFF")

    # Enable IDENTITY_INSERT for Parts table
    cursor.execute("SET IDENTITY_INSERT Parts ON")

    # Insert data into Parts table
    cursor.executemany(
        """
        INSERT INTO Parts (PartID, BikeID, PartName, Category, Price, StockQuantity)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (1, 1, 'Shimano Deore XT', 'Gear', 100, 2),
            (2, 1, 'RockShox Reba', 'Fork', 200, 5),
            (3, 1, 'Shimano Deore XT', 'Brakes', 150, 3),
            (4, 1, 'Maxxis Minion DHF', 'Tires', 50, 1),
            (5, 1, 'Shimano Deore XT', 'Gear', 100, 2),
            (6, 1, 'RockShox Reba', 'Fork', 200, 5),
            (7, 1, 'Shimano Deore XT', 'Brakes', 150, 3),
            (8, 1, 'Maxxis Minion DHF', 'Tires', 50, 1),
            (9, 1, 'Shimano Deore XT', 'Gear', 100, 2),
            (10, 1, 'RockShox Reba', 'Fork', 200, 5),
            (11, 1, 'Shimano Deore XT', 'Brakes', 150, 3),
            (12, 1, 'Maxxis Minion DHF', 'Tires', 50, 1),
        ]
    )

    # Disable IDENTITY_INSERT for Parts table
    cursor.execute("SET IDENTITY_INSERT Parts OFF")

    # Enable IDENTITY_INSERT for Orders table
    cursor.execute("SET IDENTITY_INSERT Orders ON")

    # Insert data into Orders table
    cursor.executemany(
        """
        INSERT INTO Orders (OrderID, UserID, OrderDate, TotalAmount, Status)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (1, 2, '2024-05-01', 1000, 'Delivered'),
            (2, 3, '2024-05-02', 1500, 'In Progress'),
            (3, 4, '2024-05-03', 800, 'Delivered'),
            (4, 2, '2024-05-04', 5000, 'In Progress'),
        ]
    )

    # Disable IDENTITY_INSERT for Orders table
    cursor.execute("SET IDENTITY_INSERT Orders OFF")

    # Enable IDENTITY_INSERT for OrderDetails table
    cursor.execute("SET IDENTITY_INSERT OrderDetails ON")

    # Insert data into OrderDetails table
    cursor.executemany(
        """
        INSERT INTO OrderDetails (OrderDetailID, OrderID, BikeID, PartID, Quantity, UnitPrice)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (1, 1, 1, 1, 1, 100),
            (2, 2, 2, 2, 1, 200),
            (3, 3, 3, 3, 1, 150),
            (4, 4, 4, 4, 1, 50),
        ]
    )

    # Disable IDENTITY_INSERT for OrderDetails table
    cursor.execute("SET IDENTITY_INSERT OrderDetails OFF")

    # Enable IDENTITY_INSERT for Reviews table
    cursor.execute("SET IDENTITY_INSERT Reviews ON")

    # Insert data into Reviews table
    cursor.executemany(
        """
        INSERT INTO Reviews (ReviewID, UserID, BikeID, ShopID, Rating, Comment, ReviewDate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (1, 2, 1, 1, 5, 'Great bike!', '2024-05-01'),
            (2, 3, 2, 1, 4, 'Good bike!', '2024-05-02'),
            (3, 4, 3, 1, 3, 'Nice bike!', '2024-05-03'),
            (4, 2, 4, 1, 2, 'Ok bike!', '2024-05-04'),
            (5, 2, 1, 1, 5, 'Great shop!', '2024-05-01'),
        ]
    )

    # Disable IDENTITY_INSERT for Reviews table
    cursor.execute("SET IDENTITY_INSERT Reviews OFF")

    # Commit the transaction
    conn.commit()
    print("Data inserted successfully!")

except pyodbc.Error as e:
    print("Error:", e)

finally:
    # Close the connection
    if conn:
        conn.close()