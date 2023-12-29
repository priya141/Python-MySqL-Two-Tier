import mysql.connector

def create_database():
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="test1234"
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Create the database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS amitdiwan")

    # Switch to the amitdiwan database
    cursor.execute("USE amitdiwan")

    # Check if the 'users' table exists
    cursor.execute("SHOW TABLES LIKE 'users'")
    table_exists = cursor.fetchone()

    # If the table doesn't exist, create it
    if not table_exists:
        cursor.execute("""
            CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT NOT NULL
            )
        """)

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()

def add_user(name, age):
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="test1234",
        database="amitdiwan"
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Insert user information into the 'users' table
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()

def main():
    create_database()

    while True:
        print("\n1. Add User")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            name = input("Enter user name: ")
            age = int(input("Enter user age: "))
            add_user(name, age)
            print("User added successfully!")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
