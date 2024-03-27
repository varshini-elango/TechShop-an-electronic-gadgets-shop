import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# dao/Products.py

from util.DBConnUtil import DBUtil
import pyodbc

class ProductDAO:

    def get_product_details(self, product_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "SELECT * FROM Products WHERE ProductID = ?"
            cursor.execute(query, product_id)
            product_data = cursor.fetchone()

            if product_data:
                print("Product ID:", product_data[0])
                print("Product Name:", product_data[1])
                print("Description:", product_data[2])
                print("Price:", product_data[3])
            else:
                print("Product not found.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def update_product_info(self, product_id, price=None, description=None):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            if price:
                query = "UPDATE Products SET Price = ? WHERE ProductID = ?"
                cursor.execute(query, price, product_id)
            if description:
                query = "UPDATE Products SET Description = ? WHERE ProductID = ?"
                cursor.execute(query, description, product_id)

            conn.commit()
            print("Product information updated successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def is_product_in_stock(self, product_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "SELECT QuantityInStock FROM Inventory WHERE ProductID = ?"
            cursor.execute(query, product_id)
            quantity = cursor.fetchone()

            if quantity and quantity[0] > 0:
                print("Product is in stock.")
            else:
                print("Product is out of stock.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()


    def insert_product(self,product_id, product_name, description, price):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "INSERT INTO Products (Productid,ProductName, Description, Price) VALUES (? ,?, ?, ?)"
            cursor.execute(query, product_id,product_name, description, price)

            conn.commit()
            print("Product inserted successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()
