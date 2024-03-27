import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# main_package/main.py

from dao.Customers import CustomerDAO
from dao.Products import ProductDAO
from dao.Orders import OrderDAO
from dao.OrderDetails import OrderDetailsDAO
from dao.Inventorys import InventoryDAO

def main():
    customer_dao = CustomerDAO()
    product_dao = ProductDAO()
    order_dao = OrderDAO()
    orderdetails_dao = OrderDetailsDAO()
    inventory_dao=InventoryDAO()
   
    print("1. Customers\n2. Products\n3. Orders\n4. OrderDetails\n5. Inventory\n")
    choice = input("Enter your choice: ")
        
    if choice == '1':
        print("\n1. Insert Customer\n2. Delete Customer\n3. Calculate Total Orders\n4. Get Customer Details\n5. Update Customer Info\n")
        choice_customer = input("Enter your choice: ")
        if choice_customer == '1':
         first_name = input("Enter First Name: ")
         last_name = input("Enter Last Name: ")
         email = input("Enter Email: ")
         phone = input("Enter Phone: ")
         address = input("Enter Address: ")
         customer_dao.insert_customer(first_name, last_name, email, phone, address)
        elif choice_customer == '2':
         customer_id = input("Enter Customer ID to delete: ")
         customer_dao.delete_customer(customer_id)
        elif choice_customer == '3':
         customer_id = input("Enter Customer ID: ")
         customer_dao.calculate_total_orders(customer_id)
        elif choice_customer == '4':
         customer_id = input("Enter Customer ID: ")
         customer_dao.get_customer_details(customer_id)
        elif choice_customer == '5':
         customer_id = input("Enter Customer ID: ")
         email = input("Enter New Email: ")
         phone = input("Enter New Phone: ")
         address = input("Enter New Address: ")
         customer_dao.update_customer_info(customer_id, email, phone, address)
        else:
          print("Invalid choice. Please try again.")
    
    elif choice == '2':
        print("\n1. Get Product Details\n2. Insert Product\n3. Update Product Info\n4. Check Product Stock\n")
        choice_product = input("Enter your choice: ")
        if choice_product == '1':
         product_id = input("Enter Product ID: ")
         product_dao.get_product_details(product_id)
        elif choice_product == '2':
         product_id = input("Enter Product id: ")
         product_name = input("Enter Product Name: ")
         description = input("Enter Product Description: ")
         price = input("Enter Product Price: ")
         product_dao.insert_product(product_id,product_name, description, price)
        elif choice_product == '3':
         product_id = input("Enter Product ID: ")
         price = input("Enter New Price: ")
         description = input("Enter New Description: ")
         product_dao.update_product_info(product_id, price, description)
        elif choice_product == '4':
         product_id = input("Enter Product ID: ")
         product_dao.is_product_in_stock(product_id)
        else:
            print("Invalid choice. Please try again.")
        
    elif choice == '3':
        print("\n1. Insert Order\n2. Update Order Status\n3. Cancel Order\n4.Calculate total amount\n5.Get order details")
        choice_order = input("Enter your choice: ")
        if choice_order == '1':
          order_id = input("Enter Order ID: ")
          customer_id = input("Enter Customer ID: ")
          order_date = input("Enter Order Date (YYYY-MM-DD): ")
          total_amount = input("Enter Total Amount: ")
          order_dao.insert_order(order_id, customer_id, order_date, total_amount)
        elif choice_order == '2':
         order_id = input("Enter Order ID: ")
         new_status = input("Enter New Status: ")
         order_dao.update_order_status(order_id, new_status)
        elif choice_order == '3':
         order_id = input("Enter Order ID: ")
         order_dao.cancel_order(order_id)
        elif choice == '4':
         order_id = input("Enter Order ID: ")
         order_dao.calculate_total_amount(order_id)
        elif choice == '5':
         order_id = input("Enter Order ID: ")
         order_dao.get_order_details(order_id)
        else:
            print("Invalid choice. Please try again.")

    elif choice == '4':
        print("1. Calculate SubTotal\n"
                  + "2. Order Details\n"
                  + "3. Update Quantity\n"
                  + "4. Add Discount")
        choice_order_detail = input("Enter your choice: ")
        if choice_order_detail == '1':
                order_detail_id = input("Enter Order Detail ID: ")
                orderdetails_dao.calculate_subtotal(order_detail_id)
        elif choice_order_detail == '2':
                order_detail_id = input("Enter Order Detail ID: ")
                orderdetails_dao.get_order_detail_info(order_detail_id)
        elif choice_order_detail == '3':
                order_detail_id = input("Enter Order Detail ID: ")
                new_quantity=input("Enter new quantity: ")
                orderdetails_dao.update_quantity(order_detail_id, new_quantity)
        elif choice_order_detail == '4':
                order_detail_id = input("Enter Order Detail ID: ")
                totalAfterDiscount=input("Enter total After Discount: ")
                orderdetails_dao.add_discount(order_detail_id,totalAfterDiscount)
        else:
            print("Invalid choice. Please try again.")

    elif choice == '5':
        print("1. Get Product\n"
                  + "2. Get Quantity in Stock\n"
                  + "3. Add To Inventory\n"
                  + "4. Remove From Inventory\n"
                  + "5. Update Stock Quantity\n"
                  + "6. Product Available\n"
                  + "7. Get Inventory Value\n"
                  + "8. List Low Stock Products\n"
                  + "9. List Out Of Stock Products\n"
                  + "10. List All Products")
        choice_inventory = input("Enter your choice: ")
        if choice_inventory == '1':
                 inventory_id = int(input("Enter the inventory id: "))
                 inventory_dao.get_product(inventory_id)
        elif choice_inventory == '2':
               inventory_id = int(input("Enter the inventory id: "))
               inventory_dao.get_quantity_in_stock(inventory_id)
        elif choice_inventory == '3':
                product_id = int(input("Enter the product id: "))
                quantity_in_stock= int(input("Enter the quantity in stock: "))
                last_stock_update= int(input("Enter the last stock update: "))
                inventory_dao.insert_inventory(product_id, quantity_in_stock, last_stock_update)
        elif choice_inventory == '4':
               inventory_id = int(input("Enter the inventory id: "))
               quantity=int(input("Enter the quantity: "))
               inventory_dao.remove_from_inventory(quantity, inventory_id)
        elif choice_inventory == '5':
                inventory_id = int(input("Enter the inventory id: "))
                new_quantity = int(input("Enter the new quantity: "))
                inventory_dao.update_stock_quantity(inventory_id, new_quantity)
        elif choice_inventory == '6':
                inventory_id = input("Enter Inventory ID: ")
                quantity_to_check = int(input("Enter Quantity to Check: "))
                if inventory_dao.is_product_available(inventory_id, quantity_to_check):
                 print("Product is available in inventory.")
                else:
                  print("Product is not available in inventory.")
        elif choice_inventory == '7':
                inventory_id = input("Enter Inventory ID: ")
                inventory_dao.get_inventory_value(inventory_id)
        elif choice_inventory == '8':
                threshold = int(input("Enter the threshold for low stock: "))
                inventory_dao.list_low_stock_products(threshold)
        elif choice_inventory == '9':
                inventory_dao.list_out_of_stock_products()
        elif choice_inventory == '10':
               inventory_dao.list_all_products()
        else:
            print("Invalid choice. Please try again.")

    else:
        print("Invalid choice. Please try again.")
        print("Thank you Visit Again!")


if __name__ == "__main__":
    main()
