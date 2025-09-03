"""
Car Showroom Management System
--------------------------------
Python + MySQL mini project for managing car showroom operations.
"""

import mysql.connector
from mysql.connector import Error


def get_connection():
    """Establish MySQL connection."""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword",  # replace with your MySQL password
            database="CarShowroom"
        )
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def display_models(conn):
    """Show all available car models."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM models")
    models = cursor.fetchall()
    print("\nAvailable Car Models:")
    for model in models:
        print(f"ID: {model[0]} | Model: {model[1]} | Price: ₹{model[2]}")
    cursor.close()


def place_order(conn):
    """Insert a new order."""
    try:
        model_id = int(input("Enter model ID: "))
        name = input("Enter customer name: ")
        qty = int(input("Enter quantity: "))

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO orders (model_id, customer_name, quantity) VALUES (%s,%s,%s)",
            (model_id, name, qty)
        )
        conn.commit()
        print("✅ Order placed successfully!")
        cursor.close()
    except Error as e:
        print(f"Error placing order: {e}")


def display_orders(conn):
    """Show all orders."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    print("\nAll Orders:")
    for order in orders:
        print(f"Order ID: {order[0]} | Model ID: {order[1]} | Customer: {order[2]} | Qty: {order[3]}")
    cursor.close()


def display_total_cost(conn):
    """Show total cost for each order."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT o.order_id, o.customer_name, m.model_name, o.quantity,
               (o.quantity * m.price) AS total
        FROM orders o
        JOIN models m ON o.model_id = m.model_id
    """)
    results = cursor.fetchall()
    print("\nOrder Costs:")
    for row in results:
        print(f"Order ID: {row[0]} | Customer: {row[1]} | Model: {row[2]} | Qty: {row[3]} | Total: ₹{row[4]}")
    cursor.close()


def delete_order(conn):
    """Delete an order by ID."""
    try:
        oid = int(input("Enter order ID to delete: "))
        cursor = conn.cursor()
        cursor.execute("DELETE FROM orders WHERE order_id = %s", (oid,))
        conn.commit()
        print("🗑️ Order deleted successfully!")
        cursor.close()
    except Error as e:
        print(f"Error deleting order: {e}")


def main():
    conn = get_connection()
    if not conn:
        return

    while True:
        print("\n--- Car Showroom Menu ---")
        print("1. Display available models")
        print("2. Place order")
        print("3. Display all orders")
        print("4. Display total cost")
        print("5. Delete order")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_models(conn)
            elif choice == 2:
                place_order(conn)
            elif choice == 3:
                display_orders(conn)
            elif choice == 4:
                display_total_cost(conn)
            elif choice == 5:
                delete_order(conn)
            elif choice == 6:
                print("👋 Exiting... Goodbye!")
                break
            else:
                print("❌ Invalid choice, try again!")
        except ValueError:
            print("⚠️ Please enter a number between 1-6.")

    conn.close()


if __name__ == "__main__":
    main()
