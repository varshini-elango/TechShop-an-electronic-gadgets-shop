import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# dao/OrderDetailsDAO.py

from util.DBConnUtil import DBUtil
import pyodbc

class OrderDetailsDAO:

    def get_order_detail_info(self, order_detail_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = """
                    SELECT OrderDetails.OrderDetailID, Orders.OrderID, Products.ProductID, Products.ProductName, OrderDetails.Quantity
                    FROM OrderDetails
                    INNER JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
                    INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
                    WHERE OrderDetails.OrderDetailID = ?
                    """
            cursor.execute(query, order_detail_id)
            order_detail_info = cursor.fetchone()

            if order_detail_info:
                order_detail_id, order_id, product_id, product_name, quantity = order_detail_info
                print(f"Order Detail ID: {order_detail_id}")
                print(f"Order ID: {order_id}")
                print(f"Product ID: {product_id}")
                print(f"Product Name: {product_name}")
                print(f"Quantity: {quantity}")
            else:
                print("Order detail not found.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def update_quantity(self, order_detail_id, new_quantity):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "UPDATE OrderDetails SET Quantity = ? WHERE OrderDetailID = ?"
            cursor.execute(query, new_quantity, order_detail_id)

            conn.commit()
            print("Quantity updated successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def calculate_subtotal(self, order_detail_id):
        try:
           conn = DBUtil.getDBConn()
           cursor = conn.cursor()

           query = """
                    SELECT Products.Price, OrderDetails.Quantity
                    FROM OrderDetails
                    INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
                    WHERE OrderDetails.OrderDetailID = ?
                    """
           cursor.execute(query, order_detail_id)
           price, quantity = cursor.fetchone()

           subtotal = price * quantity
           print("Subtotal:", subtotal)
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def add_discount(self, order_detail_id, discount_amount ,discountPercentage):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query ="SELECT Quantity, p.Price FROM OrderDetails od JOIN Products p ON od.ProductID = p.ProductID WHERE OrderDetailID = ?"
            cursor.execute(query, order_detail_id)
            price, quantity = cursor.fetchone()

            totalBeforeDiscount = quantity * price
            discount_amount = totalBeforeDiscount * (discountPercentage / 100)
            totalAfterDiscount = totalBeforeDiscount - discount_amount

            query="UPDATE Order SET Totalamount = ? WHERE OrderID = ?"
            cursor.execute(query,totalAfterDiscount, order_detail_id)
            conn.commit()
            if self.rowcount > 0:
                  print("Discount applied successfully. New total price:", totalAfterDiscount)
            else:
                  print("Failed to apply discount.")
          
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()


    

    

   
