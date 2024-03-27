import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.DBConnUtil import DBUtil

class Implementation:
    def __init__(self):
        self.db_connection = None
        self.db_cursor = None

    def connect_to_db(self):
        try:
            self.db_connection = DBUtil.getDBConn() 
            if self.db_connection:
                print("Connected to the database")
                self.db_cursor = self.db_connection.cursor()
        except Exception as e:
            print("Error while connecting to SQL Server:", e)

    
    def insert_customer(self, customer):
        try:
            print("Inserting customer...")
            query = "INSERT INTO Customers (CustomerId, FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?, ?)"
            self.db_cursor.execute(query, (customer["CustomerId"], customer["FirstName"], customer["LastName"], customer["Email"], customer["Phone"], customer["Address"]))
            self.db_connection.commit()
            print("Customer inserted successfully.")
        except Exception as e:
            print("Error inserting customer:", e)

    def validate_customer(self, customer_id):
        try:
            print("Validating customer...")
            query = "SELECT COUNT(*) FROM Customers WHERE CustomerId = ?"
            self.db_cursor.execute(query, (customer_id,))
            result = self.db_cursor.fetchone()
            if result[0] > 0:
                return True
            else:
                return False
        except Exception as e:
            print("Error validating customer:", e)
            return False

    def insert_orders(self, order):
        try:
            print("Inserting orders...")
            query = "INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?, ?)"
            self.db_cursor.execute(query, (order["OrderID"], order["CustomerID"], order["OrderDate"], order["TotalAmount"]))
            self.db_connection.commit()
            print("Order inserted successfully.")
        except Exception as e:
            print("Error inserting orders:", e)

    def validate_order(self, order_id):
        try:
            print("Validating order...")
            query = "SELECT COUNT(*) FROM Orders WHERE OrderID = ?"
            self.db_cursor.execute(query, (order_id,))
            result = self.db_cursor.fetchone()
            if result[0] > 0:
                return True
            else:
                return False
        except Exception as e:
            print("Error validating order:", e)
            return False

    def insert_products(self, product):
        try:
            print("Inserting products...")
            query = "INSERT INTO Products (ProductId, ProductName, Description, Price) VALUES (?, ?, ?, ?)"
            self.db_cursor.execute(query, (product["ProductId"], product["ProductName"], product["Description"], product["Price"]))
            self.db_connection.commit()
            print("Product inserted successfully.")
        except Exception as e:
            print("Error inserting product:", e)

    def validate_product(self, product_id):
        try:
            print("Validating product...")
            query = "SELECT COUNT(*) FROM Products WHERE ProductId = ?"
            self.db_cursor.execute(query, (product_id,))
            result = self.db_cursor.fetchone()
            if result[0] > 0:
                return True
            else:
                return False
        except Exception as e:
            print("Error validating product:", e)
            return False

    def insert_inventory(self, inventory):
        try:
            print("Inserting inventory...")
            query = "INSERT INTO Inventory (InventoryID, ProductID, QuantityInStock, LastStockUpdate) VALUES (?, ?, ?, ?)"
            self.db_cursor.execute(query, (inventory["InventoryID"], inventory["ProductID"], inventory["QuantityInStock"], inventory["LastStockUpdate"]))
            self.db_connection.commit()
            print("Inventory inserted successfully.")
        except Exception as e:
            print("Error inserting inventory:", e)

    def validate_inventory(self, inventory_id):
        try:
            print("Validating inventory...")
            query = "SELECT COUNT(*) FROM Inventory WHERE InventoryID = ?"
            self.db_cursor.execute(query, (inventory_id,))
            result = self.db_cursor.fetchone()
            if result[0] > 0:
                return True
            else:
                return False
        except Exception as e:
            print("Error validating inventory:", e)
            return False

    def delete_customer(self, customer_id):
        try:
            print("Deleting customer...")
            query = "DELETE FROM Customers WHERE CustomerId = ?"
            self.db_cursor.execute(query, (customer_id,))
            self.db_connection.commit()
            print("Customer deleted successfully.")
        except Exception as e:
            print("Error deleting customer:", e)