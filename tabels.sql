-- Create the database
CREATE DATABASE BikeShopDB;
GO

-- Use the created database
USE BikeShopDB;
GO

-- Create Users table
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) NOT NULL UNIQUE,
    PasswordHash NVARCHAR(255) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    PhoneNumber NVARCHAR(15),
    JoinDate DATETIME DEFAULT GETDATE()
);
GO

-- Create BikeShops table
CREATE TABLE BikeShops (
    ShopID INT PRIMARY KEY IDENTITY(1,1),
    ShopName NVARCHAR(100) NOT NULL,
    Location NVARCHAR(255) NOT NULL,
    PhoneNumber NVARCHAR(15),
    OwnerID INT NOT NULL,
    FOREIGN KEY (OwnerID) REFERENCES Users(UserID)
);
GO

-- Create Bikes table
CREATE TABLE Bikes (
    BikeID INT PRIMARY KEY IDENTITY(1,1),
    ShopID INT NOT NULL,
    Model NVARCHAR(100) NOT NULL,
    Brand NVARCHAR(100),
    Type NVARCHAR(50),  -- Mountain, Road, Electric, etc.
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT DEFAULT 0,
    FOREIGN KEY (ShopID) REFERENCES BikeShops(ShopID)
);
GO

-- Create Parts table
CREATE TABLE Parts (
    PartID INT PRIMARY KEY IDENTITY(1,1),
    BikeID INT NOT NULL,
    PartName NVARCHAR(100) NOT NULL,
    Category NVARCHAR(50),  -- Brakes, Tires, Gears, etc.
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT DEFAULT 0,
    FOREIGN KEY (BikeID) REFERENCES Bikes(BikeID)
);
GO

-- Create Orders table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT NOT NULL,
    OrderDate DATETIME DEFAULT GETDATE(),
    TotalAmount DECIMAL(10, 2) NOT NULL,
    Status NVARCHAR(50) DEFAULT 'Pending',  -- Pending, Shipped, Delivered
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
GO

-- Create OrderDetails table
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY IDENTITY(1,1),
    OrderID INT NOT NULL,
    BikeID INT NULL,  -- Nullable to allow either Bike or Part
    PartID INT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    Subtotal AS (Quantity * UnitPrice),  -- Computed column
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (BikeID) REFERENCES Bikes(BikeID),
    FOREIGN KEY (PartID) REFERENCES Parts(PartID)
);
GO

-- Create Reviews table
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT NOT NULL,
    BikeID INT NULL,
    ShopID INT NULL,
    Rating INT CHECK (Rating >= 1 AND Rating <= 5),
    Comment NVARCHAR(1000),
    ReviewDate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (BikeID) REFERENCES Bikes(BikeID),
    FOREIGN KEY (ShopID) REFERENCES BikeShops(ShopID)
);
GO
