import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# dao/InventoryDAO.py

from util.DBConnUtil import DBUtil
import pyodbc

class InventoryDAO:

    def get_product(self, inventory_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = """
                    SELECT Products.ProductID, Products.ProductName, Products.Description, Products.Price
                    FROM Inventory
                    INNER JOIN Products ON Inventory.ProductID = Products.ProductID
                    WHERE Inventory.InventoryID = ?
                    """
            cursor.execute(query, inventory_id)
            product_info = cursor.fetchone()

            if product_info:
                product_id, product_name, description, price = product_info
                return {"ProductID": product_id, "ProductName": product_name, "Description": description, "Price": price}
            else:
                return None
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def get_quantity_in_stock(self, inventory_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "SELECT QuantityInStock FROM Inventory WHERE InventoryID = ?"
            cursor.execute(query, inventory_id)
            quantity_in_stock = cursor.fetchone()[0]

            return quantity_in_stock
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def remove_from_inventory(self, inventory_id, quantity):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()
            query = "UPDATE Inventory SET QuantityInStock = QuantityInStock - ? WHERE InventoryID = ?"
            cursor.execute(query, quantity, inventory_id)

            conn.commit()
            print("Quantity removed from inventory successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def update_stock_quantity(self, inventory_id, new_quantity):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "UPDATE Inventory SET QuantityInStock = ? WHERE InventoryID = ?"
            cursor.execute(query, new_quantity, inventory_id)

            conn.commit()
            print("Stock quantity updated successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def is_product_available(self, inventory_id, quantity_to_check):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "SELECT QuantityInStock FROM Inventory WHERE InventoryID = ?"
            cursor.execute(query, inventory_id)
            quantity_in_stock = cursor.fetchone()[0]

            return quantity_in_stock >= quantity_to_check
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def get_inventory_value(self, inventory_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = """
                    SELECT Products.Price, Inventory.QuantityInStock
                    FROM Inventory
                    INNER JOIN Products ON Inventory.ProductID = Products.ProductID
                    WHERE Inventory.InventoryID = ?
                    """
            cursor.execute(query, inventory_id)
            price, quantity_in_stock = cursor.fetchone()

            return price * quantity_in_stock
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def list_low_stock_products(self, threshold):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = """
                    SELECT Products.ProductName, Inventory.QuantityInStock
                    FROM Inventory
                    INNER JOIN Products ON Inventory.ProductID = Products.ProductID
                    WHERE Inventory.QuantityInStock < ?
                    """
            cursor.execute(query, threshold)
            low_stock_products = cursor.fetchall()

            print("Low Stock Products:")
            for product_name, quantity_in_stock in low_stock_products:
                print(f"Product: {product_name}, Quantity in Stock: {quantity_in_stock}")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def list_out_of_stock_products(self):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = """
                    SELECT Products.ProductName
                    FROM Inventory
                    INNER JOIN Products ON Inventory.ProductID = Products.ProductID
                    WHERE Inventory.QuantityInStock = 0
                    """
            cursor.execute(query)
            out_of_stock_products = cursor.fetchall()

            print("Out of Stock Products:")
            for product_name in out_of_stock_products:
                print(product_name[0])
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def list_all_products(self):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = """
                    SELECT Products.ProductName, Inventory.QuantityInStock
                    FROM Inventory
                    INNER JOIN Products ON Inventory.ProductID = Products.ProductID
                    """
            cursor.execute(query)
            all_products = cursor.fetchall()

            print("All Products in Inventory:")
            for product_name, quantity_in_stock in all_products:
                print(f"Product: {product_name}, Quantity in Stock: {quantity_in_stock}")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def insert_inventory(self, product_id, quantity_in_stock, last_stock_update):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "INSERT INTO Inventory (ProductID, QuantityInStock, LastStockUpdate) VALUES (?, ?, ?)"
            cursor.execute(query, product_id, quantity_in_stock, last_stock_update)

            conn.commit()
            print("Inventory item inserted successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()


    