import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# dao/OrderDAO.py

from util.DBConnUtil import DBUtil
import pyodbc

class OrderDAO:

    def insert_order(self, order_id, customer_id, order_date, total_amount):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?, ?)"
            cursor.execute(query, order_id, customer_id, order_date, total_amount)

            conn.commit()
            print("Order inserted successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()


    def get_order_details(self, order_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()
            query = """
                    SELECT Products.ProductName, OrderDetails.Quantity
                    FROM OrderDetails
                    INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
                    WHERE OrderDetails.OrderID = ?
                    """
            cursor.execute(query, order_id)
            order_details = cursor.fetchall()

            if order_details:
                print("Order Details for Order ID:", order_id)
                for product_name, quantity in order_details:
                    print(f"Product: {product_name}, Quantity: {quantity}")
            else:
                print("No details found for Order ID:", order_id)
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

   
    def update_order_status(self, order_id, new_status):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "UPDATE Orders SET Status = ? WHERE OrderID = ?"
            cursor.execute(query, new_status, order_id)

            conn.commit()
            print("Order status updated successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def cancel_order(self, order_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "UPDATE orders SET state = 'Cancelled' WHERE orderid = ?"
            cursor.execute(query,order_id)

            print("Order canceled successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def calculate_total_amount(self, order_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = """
                    SELECT SUM(Products.Price * OrderDetails.Quantity) AS TotalAmount
                    FROM OrderDetails
                    INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
                    WHERE OrderDetails.OrderID = ?
                    """
            cursor.execute(query, order_id)
            total_amount = cursor.fetchone()[0]

            print("Total Amount:", total_amount)
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()
  
