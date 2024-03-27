import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# dao/Customers.py

from util.DBConnUtil import DBUtil
import pyodbc

class CustomerDAO:
    
    def calculate_total_orders(self, customer_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "SELECT COUNT(*) FROM Orders WHERE CustomerID = ?"
            cursor.execute(query, customer_id)
            total_orders = cursor.fetchone()[0]

            print("Total Orders:", total_orders)
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def get_customer_details(self, customer_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "SELECT * FROM Customers WHERE CustomerID = ?"
            cursor.execute(query, customer_id)
            customer_data = cursor.fetchone()

            if customer_data:
                print("Customer ID:", customer_data[0])
                print("Name:", customer_data[1], customer_data[2])
                print("Email:", customer_data[3])
                print("Phone:", customer_data[4])
                print("Address:", customer_data[5])
            else:
                print("Customer not found.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def update_customer_info(self, customer_id, email=None, phone=None, address=None):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            if email:
                query = "UPDATE Customers SET Email = ? WHERE CustomerID = ?"
                cursor.execute(query, email, customer_id)
            if phone:
                query = "UPDATE Customers SET Phone = ? WHERE CustomerID = ?"
                cursor.execute(query, phone, customer_id)
            if address:
                query = "UPDATE Customers SET Address = ? WHERE CustomerID = ?"
                cursor.execute(query, address, customer_id)

            conn.commit()
            print("Customer information updated successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()


    def insert_customer(self, first_name, last_name, email, phone, address):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, first_name, last_name, email, phone, address)

            conn.commit()
            print("Customer inserted successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def delete_customer(self, customer_id):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            query = "DELETE FROM Customers WHERE CustomerID = ?"
            cursor.execute(query, customer_id)

            conn.commit()
            print("Customer deleted successfully.")
        except pyodbc.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()