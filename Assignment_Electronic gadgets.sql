/*Task 1*/
create database TechShop;
use TechShop;
create table Customers(
CustomerId int Identity constraint C_PK Primary Key,
FirstName varchar(45) not null,
LastName varchar(40),
email varchar(65) not null,
phone varchar(20),
Address varchar(80) not null);

INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES 
    ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
    ('Jane', 'Smith', 'jane.smith@example.com', NULL, '456 Elm St'),
    ('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567', '789 Oak St'),
    ('Michael', 'Brown', 'michael.brown@example.com', '444-555-6666', '321 Pine St'),
    ('Emily', 'Taylor', 'emily.taylor@example.com', NULL, '654 Birch St'),
    ('David', 'Martinez', 'david.martinez@example.com', '777-888-9999', '987 Cedar St'),
    ('Sarah', 'Anderson', 'sarah.anderson@example.com', NULL, '741 Maple St'),
    ('Christopher', 'Wilson', 'christopher.wilson@example.com', '222-333-4444', '852 Walnut St'),
    ('Jessica', 'Thomas', 'jessica.thomas@example.com', '999-888-7777', '369 Oak St'),
    ('Matthew', 'Lee', 'matthew.lee@example.com', '111-222-3333', '963 Elm St');
	select * from Customers;

	use TechShop;
	CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Description VARCHAR(MAX),
    Price DECIMAL(10, 2)
);

INSERT INTO Products (ProductID, ProductName, Description, Price)
VALUES
(1, 'Laptop', '15.6-inch Full HD display, 8GB RAM, 256GB SSD', 799.99),
(2, 'Smartphone', '6.5-inch AMOLED display, 128GB storage, 4000mAh battery', 699.00),
(3, 'Tablet', '10.2-inch Retina display, 64GB storage, Wi-Fi + Cellular', 449.99),
(4, 'Headphones', 'Noise-cancelling, Bluetooth, 30-hour battery life', 149.95),
(5, 'Smartwatch', 'Water-resistant, heart rate monitor, GPS', 199.99),
(6, 'Camera', '24.2MP sensor, 4K video recording, Wi-Fi connectivity', 899.00),
(7, 'Printer', 'All-in-one, color printing, wireless', 249.99),
(8, 'Desktop Computer', 'Intel Core i7 processor, 16GB RAM, 1TB SSD', 1299.99),
(9, 'External Hard Drive', '2TB capacity, USB 3.0 interface, portable', 79.99),
(10, 'Wireless Mouse', 'Ergonomic design, 1600 DPI, long battery life', 29.95);

select * from Products;

use TechShop;

	CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    OrderDate DATE,
    TotalAmount DECIMAL(10, 5),
);

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount)
VALUES
(1, 1, '01-02-2024', 1000),
(2, 2, '02-02-2024', 2000),
(3, 3, '03-02-2024', 3000),
(4, 4, '04-02-2024', 4000),
(5, 5, '05-02-2024', 5000),
(6, 6, '06-02-2024', 6000),
(7, 7, '07-02-2024', 7000),
(8, 8, '08-02-2024', 8000),
(9, 9, '09-02-2024', 9000),
(10, 10, '10-02-2024', 10000);
select * from Orders; 


CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES
(1, 1, 1, 3),
(2, 2, 2, 2),
(3, 3, 3, 1),
(4, 4, 4, 4),
(5, 5, 5, 2),
(6, 6, 6, 3),
(7, 7, 7, 1),
(8, 8, 8, 2),
(9, 9, 9, 5),
(10,10, 10, 1);
select * from OrderDetails;

CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY,
    ProductID INT,
    QuantityInStock INT,
    LastStockUpdate DATE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Inventory (InventoryID, ProductID, QuantityInStock, LastStockUpdate)
VALUES
(1, 1, 100, '2024-01-10'),
(2, 2, 75, '2024-01-11'),
(3, 3, 50, '2024-01-12'),
(4, 4, 200, '2024-01-13'),
(5, 5, 150, '2024-01-14'),
(6, 6, 120, '2024-01-15'),
(7, 7, 80, '2024-01-16'),
(8, 8, 90, '2024-01-17'),
(9, 9, 110, '2024-01-18'),
(10, 10, 60, '2024-01-19');
select * from Inventory;

CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(255),
    ProductID INT,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
INSERT INTO Categories (CategoryID, CategoryName, ProductID)
VALUES
    (1, 'Category A', 1),
    (2, 'Category A', 2),
    (3, 'Category B', 3),
    (4, 'Category B', 4),
    (5, 'Category C', 5),
    (6, 'Category C', 6),
    (7, 'Category D', 7),
    (8, 'Category D', 8),
    (9, 'Category E', 9),
    (10, 'Category E', 10),
    (11, 'Category F', 11);
	select * from Categories;


/*Task 2*/
/*1. Write an SQL query to retrieve the names and emails of all customers.*/
select FirstName,LastName,email from customers;

/*2.Write an SQL query to list all orders with their order dates and corresponding customer names.*/
SELECT o.OrderID, o.OrderDate, CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID;

/*3. Write an SQL query to insert a new customer record into the "Customers" table. Include 
customer information such as name, email, and address.*/
INSERT INTO Customers(FirstName, LastName, email, Address)
VALUES ('Emma', 'Johnson', 'emma.johnson@example.com', '456 Elm St, Springfield, USA');

/*4. Write an SQL query to update the prices of all electronic gadgets in the "Products" table by 
increasing them by 10%.*/
UPDATE Products
SET Price = Price * 1.10;

/*5. Write an SQL query to delete a specific order and its associated order details from the 
"Orders" and "OrderDetails" tables. Allow users to input the order ID as a parameter.
*/

DECLARE @OrderID INT= 4;
DELETE FROM OrderDetails
WHERE OrderID =@OrderID ;
DELETE FROM Orders
WHERE OrderID = @OrderID ;

/*6. Write an SQL query to insert a new order into the "Orders" table. Include the customer ID, 
order date, and any other necessary information*/
INSERT INTO Orders (CustomerID, OrderID, OrderDate, TotalAmount)
VALUES (11, 11, '2024-02-28', 1500.99);

/*7. Write an SQL query to update the contact information (e.g., email and address) of a specific 
customer in the "Customers" table. Allow users to input the customer ID and new contact 
information.*/

--UPDATE Customers SET Email = 'new1@gmail.com',Address = 'TamilNadu' WHERE CustomerID = 3;
use TechShop;

DECLARE @CustomerIDToUpdate int=2;
DECLARE @NewEmail VARCHAR(65)='varsh@example.com';
DECLARE @NewAddress VARCHAR(80)='25 street';
UPDATE Customers
SET email = @NewEmail,
    Address = @NewAddress
WHERE Customerid = @CustomerIDToUpdate;

/*8. Write an SQL query to recalculate and update the total cost of each order in the "Orders" 
table based on the prices and quantities in the "OrderDetails" table.*/
UPDATE Orders
SET TotalAmount = (
    SELECT sum(OD.Quantity * P.Price)
    FROM OrderDetails OD
    JOIN Products P ON OD.ProductID = P.ProductID
    WHERE OD.OrderID = Orders.OrderID
)
select*from orders;
/*
UPDATE Orders
SET TotalAmount = (
    SELECT SUM(Quantity * Price)
    FROM OrderDetails od
    JOIN Products p ON od.ProductID = p.ProductID
    WHERE od.OrderID = Orders.OrderID
)
WHERE OrderID IN (
    SELECT OrderID
    FROM OrderDetails
);*/

/*9. Write an SQL query to delete all orders and their associated order details for a specific 
customer from the "Orders" and "OrderDetails" tables. Allow users to input the customer ID 
as a parameter.*/

DECLARE @CustomerIDToDelete INT;
SET @CustomerIDToDelete = 5; -- Replace with the specific customer ID

BEGIN TRANSACTION;

-- Delete from OrderDetails table
DELETE FROM OrderDetails
WHERE OrderID IN (
    SELECT OrderID
    FROM Orders
    WHERE CustomerID = @CustomerIDToDelete
);

-- Delete from Orders table
DECLARE @CustomerIDToDelete INT;
SET @CustomerIDToDelete = 5;
DELETE FROM Orders
WHERE CustomerID = @CustomerIDToDelete;

COMMIT TRANSACTION;

/*10. Write an SQL query to insert a new electronic gadget product into the "Products" table, 
including product name, category, price, and any other relevant details.*/
INSERT INTO Products (ProductID, ProductName, Description, Price)
VALUES ('11','Jammer', 'Intel Core i7 processor, 16GB RAM, 1TB SSD', 299.99);

/*11. Write an SQL query to update the status of a specific order in the "Orders" table (e.g., from 
"Pending" to "Shipped"). Allow users to input the order ID and the new status*/
ALTER TABLE Orders
ADD Status VARCHAR(50);

DECLARE @OrderID INT = 7;
DECLARE @NewStatus VARCHAR(50)='Shipped';
UPDATE Orders
SET Status = @NewStatus
WHERE OrderID = @OrderID;

/*12. Write an SQL query to calculate and update the number of orders placed by each customer
in the "Customers" table based on the data in the "Orders" table.*/
alter table Customers
add NoOfOrders int;
update Customers
set NoOfOrders=(
select count(ORderID)
from Orders
where ORders.CustomerID=Customers.CustomerId);
select * from Customers;

/*Task 3*/
/*1.Write an SQL query to retrieve a list of all orders along with customer information (e.g., customer name) for each order.*/
SELECT o.OrderID, o.OrderDate, o.TotalAmount,c.FirstName 
AS CustomerFirstName, c.LastName AS CustomerLastName, c.Email 
AS CustomerEmail, c.Phone AS CustomerPhone, c.Address AS CustomerAddress
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID;

/*2. Write an SQL query to find the total revenue generated by each electronic gadget product. Include the product name and the total revenue.*/ 
use TechShop;
SELECT p.ProductName, SUM(od.Quantity * p.Price) AS TotalRevenue
FROM Products p
JOIN OrderDetails od ON p.ProductID = od.ProductID
JOIN Orders o ON od.OrderID = o.OrderID
GROUP BY p.ProductName;

/*3. Write an SQL query to list all customers who have made at least one purchase. Include their names and contact information. */
SELECT c.FirstName, c.LastName, c.Email, c.Phone, c.Address
FROM Customers c
WHERE EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.CustomerID = c.CustomerID
);

/*4. Write an SQL query to find the most popular electronic gadget, which is the one with the highest total quantity ordered. 
Include the product name and the total quantity ordered. */
SELECT TOP 1 p.ProductName, SUM(od.Quantity) AS TotalQuantityOrdered
FROM Products p
JOIN OrderDetails od ON p.ProductID = od.ProductID
JOIN Orders o ON od.OrderID = o.OrderID
GROUP BY p.ProductName
ORDER BY TotalQuantityOrdered DESC;

/*5. Write an SQL query to retrieve a list of electronic gadgets along with their corresponding categories.*/
SELECT ProductName,Description
FROM Products

SELECT p.ProductName,p.Description,c.CategoryName
FROM Products p
JOIN Categories c ON p.ProductID = c.ProductID

/*6. Write an SQL query to calculate the average order value for each customer. Include the customer's name and their average order value. */
SELECT c.FirstName,c.LastName,AVG(o.TotalAmount) AS AverageOrderValue
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName, c.LastName;

/*7. Write an SQL query to find the order with the highest total revenue. Include the order ID, customer information, and the total revenue.*/
SELECT TOP 1 o.OrderID,c.FirstName,c.LastName,c.Email,c.Phone,c.Address,
MAX(o.TotalAmount) AS TotalRevenue
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY o.OrderID,c.FirstName,c.LastName,c.Email,c.Phone,c.Address
ORDER BY TotalRevenue DESC;

/*8. Write an SQL query to list electronic gadgets and the number of times each product has been ordered. */
SELECT p.ProductID,p.ProductName,COUNT(od.OrderID) AS OrderCount
FROM Products p
JOIN OrderDetails od ON p.ProductID = od.ProductID
GROUP BY p.ProductID,p.ProductName;

/*9. Write an SQL query to find customers who have purchased a specific electronic gadget product. 
Allow users to input the product name as a parameter. */
DECLARE @ProductName VARCHAR(100);
SET @ProductName = 'Printer'; 

SELECT DISTINCT c.CustomerID,c.FirstName,c.LastName,c.Email,c.Phone,c.Address
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.ProductName = @ProductName;

/*10. Write an SQL query to calculate the total revenue generated by all orders placed within a specific time period. Allow users to input the
start and end dates as parameters.*/
DECLARE @StartDate DATE;
DECLARE @EndDate DATE;

SET @StartDate = '2024-02-01'; 
SET @EndDate = '2024-02-03'; 

SELECT SUM(o.TotalAmount) AS TotalRevenue
FROM Orders o
WHERE o.OrderDate >= @StartDate
AND o.OrderDate <= @EndDate;

/*Task 4*/
/*1. Write an SQL query to find out which customers have not placed any orders.*/
SELECT CustomerID,FirstName,LastName,Email,Phone,Address
FROM Customers
WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);

/*2. Write an SQL query to find the total number of products available for sale.*/ 
SELECT COUNT(*) AS TotalProducts
FROM Products;

/*3. Write an SQL query to calculate the total revenue generated by TechShop.*/
SELECT SUM(TotalAmount) AS TotalRevenue
FROM Orders;

/*4. Write an SQL query to calculate the average quantity ordered for products in a specific category. 
Allow users to input the category name as a parameter.*/
DECLARE @CategoryName VARCHAR(100);
SET @CategoryName = 'Category A';
SELECT AVG(od.Quantity) AS AverageQuantityOrdered
FROM OrderDetails od
WHERE od.ProductID IN (SELECT p.ProductID 
FROM Products p 
JOIN Categories c ON p.ProductID = c.ProductID 
WHERE c.CategoryName = @CategoryName);

/*5. Write an SQL query to calculate the total revenue generated by a specific customer.
Allow users to input the customer ID as a parameter.*/
DECLARE @CustomerID INT;
SET @CustomerID = 2;
SELECT SUM(TotalAmount) AS TotalRevenue
FROM Orders
WHERE CustomerID = @CustomerID;

/*6. Write an SQL query to find the customers who have placed the most orders. 
List their names and the number of orders they've placed.*/
SELECT c.FirstName,c.LastName,
COUNT(o.OrderID) AS NumberOfOrders
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName,c.LastName
HAVING COUNT(o.OrderID) = (SELECT MAX(OrdersCount) 
FROM (SELECT COUNT(OrderID) AS OrdersCount 
FROM Orders GROUP BY CustomerID) AS OrderCounts);

/*7. Write an SQL query to find the most popular product category, 
which is the one with the highest total quantity ordered across all orders.*/
SELECT TOP 1 p.ProductName,
SUM(od.Quantity) AS TotalQuantityOrdered
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalQuantityOrdered DESC;

/*8. Write an SQL query to find the customer who has spent the most money (highest total revenue) on electronic gadgets.
List their name and total spending.*/ 
SELECT TOP 1 c.FirstName,c.LastName,
SUM(od.Quantity * p.Price) AS TotalSpending
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY c.FirstName,c.LastName
ORDER BY TotalSpending DESC;

/*9. Write an SQL query to calculate the average order value (total revenue divided by the number of orders) for all customers.*/ 
SELECT AVG(TotalAmount) AS AverageOrderValue
FROM Orders;

/*10. Write an SQL query to find the total number of orders placed by each customer and list their names along with the order count.*/
SELECT c.FirstName,c.LastName,
COUNT(o.OrderID) AS OrderCount
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName,c.LastName;

SELECT CASE order_status         WHEN 1 THEN 'Pending'WHEN 2 THEN 'Processing'WHEN 3 THEN 'Rejected'WHEN 4 THEN 'Completed'END AS order_status,     COUNT(order_id) order_countFROM         sales.ordersWHEREYEAR(order_date) = 2018GROUP BY     order_status;

SELECT    
    SUM(CASE
            WHEN order_status = 1
            THEN 1
            ELSE 0
        END) AS 'Pending', 
    SUM(CASE
            WHEN order_status = 2
            THEN 1
            ELSE 0
        END) AS 'Processing', 
    SUM(CASE
            WHEN order_status = 3
            THEN 1
            ELSE 0
        END) AS 'Rejected', 
    SUM(CASE
            WHEN order_status = 4
            THEN 1
            ELSE 0
        END) AS 'Completed', 
    COUNT(*) AS Total
FROM    
    sales.orders
WHERE 
    YEAR(order_date) = 2018;

[14:15] Sanjith (Guest)
SELECT    

    o.order_id, 

    SUM(quantity * list_price) order_value,

    CASE

        WHEN SUM(quantity * list_price) <= 500 

            THEN 'Very Low'

        WHEN SUM(quantity * list_price) > 500 AND 

            SUM(quantity * list_price) <= 1000 

            THEN 'Low'

        WHEN SUM(quantity * list_price) > 1000 AND 

            SUM(quantity * list_price) <= 5000 

            THEN 'Medium'

        WHEN SUM(quantity * list_price) > 5000 AND 

            SUM(quantity * list_price) <= 10000 

            THEN 'High'

        WHEN SUM(quantity * list_price) > 10000 

            THEN 'Very High'

    END order_priority

FROM    

    sales.orders o

INNER JOIN sales.order_items i ON i.order_id = o.order_id

WHERE 

    YEAR(order_date) = 2018

GROUP BY 

    o.order_id;

SELECT 
    first_name,
    last_name,
    hire_date,
    CASE (2000 - CAST(strftime('%Y',hire_date) AS INTEGER))
        WHEN 1 THEN '1 year'
        WHEN 3 THEN '3 years'
        WHEN 5 THEN '5 years'
        WHEN 10 THEN '10 years'
        WHEN 15 THEN '15 years'
        WHEN 20 THEN '20 years'
        WHEN 25 THEN '25 years'
        WHEN 30 THEN '30 years'
    END aniversary
FROM
    employees
ORDER BY first_name;
SELECT      first_name,     last_name, ... by Sanjith (Unverified)
Sanjith (Unverified)
14:19
SELECT 
    first_name,
    last_name,
    CASE
        WHEN salary < 3000 THEN 'Low'
        WHEN salary >= 3000 AND salary <= 5000 THEN 'Average'
        WHEN salary > 5000 THEN 'High'
    END evaluation
FROM
    employees;



