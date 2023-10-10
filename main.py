import os
import mysql.connector

HOST = os.environ.get('DB_HOST')
DATABASE = os.environ.get('DB_NAME')
USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')

def get_connection():
    return mysql.connector.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)

# CREATE TABLES
def create_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                total_amount DECIMAL(10, 2),
                order_date DATE
            )
        """)
        conn.commit()

# INSERT SAMPLE DATA
def insert_sample_data():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 28), ('Bob', 32)")
        cursor.execute("INSERT INTO orders (user_id, total_amount, order_date) VALUES (1, 100.50, '2023-01-15'), (2, 75.20, '2023-01-16')")
        conn.commit()

def complex_sql_query():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT u.name, u.age, SUM(o.total_amount) AS total_order_amount
            FROM users u
            LEFT JOIN orders o ON u.id = o.user_id
            GROUP BY u.id, u.name, u.age
            ORDER BY u.age;
        """)
        return cursor.fetchall()

if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    
    results = complex_sql_query()
    for row in results:
        print(row)
