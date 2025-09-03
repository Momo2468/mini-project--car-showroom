"""
Car Showroom Management System
--------------------------------
Python + MySQL mini project for managing car showroom operations.
"""

import mysql.connector as sql

# Connect to MySQL
con = sql.connect(
    host="localhost",
    user="root",
    passwd="yourpassword",  # change this to your MySQL password
    database="showroom"
)

cur = con.cursor()

def display_models():
    cur.execute("SELECT * FROM cars")
    data = cur.fetchall()
    print("\nAvailable Car Models:\n")
    for row in data:
        print(row)

def place_order():
    model = input("Enter car model to order: ")
    name = input("Enter customer name: ")
    phone = int(input("Enter phone number: "))
    cur.execute("INSERT INTO customerdetails VALUES (%s,%s,%s)", (model, name, phone))
    con.commit()
    print("Order placed successfully!")

def display_orders():
    cur.execute("SELECT * FROM customerdetails")
    data = cur.fetchall()
    print("\nCustomer Orders:\n")
    for row in data:
        print(row)

def delete_order():
    name = input("Enter customer name to delete order: ")
    cur.execute("DELETE FROM customerdetails WHERE cust_name=%s", (name,))
    con.commit()
    print("Order deleted successfully!")

# Menu
while True:
    print("\n--- Car Showroom Menu ---")
    print("1. Display available models")
    print("2. Place order")
    print("3. Display orders")
    print("4. Delete order")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        display_models()
    elif ch == 2:
        place_order()
    elif ch == 3:
        display_orders()
    elif ch == 4:
        delete_order()
    elif ch == 5:
        break
    else:
        print("Invalid choice!")
