import sqlite3

# Function to create a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('product_reviews.db')
    return conn

# Function to create the products table and insert sample data
def create_products_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       price REAL NOT NULL)''')
    products = [
        ('Product 1', 10.99),
        ('Product 2', 20.99),
        # Add more sample products as needed
    ]
    cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', products)
    conn.commit()
    conn.close()

# Function to create the reviews table and insert sample data
def create_reviews_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reviews
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       product_id INTEGER NOT NULL,
                       rating INTEGER NOT NULL,
                       comment TEXT,
                       FOREIGN KEY (product_id) REFERENCES products(id))''')
    reviews = [
        (1, 4, 'Great product!'),
        (2, 5, 'Amazing!'),
        # Add more sample reviews as needed
    ]
    cursor.executemany('INSERT INTO reviews (product_id, rating, comment) VALUES (?, ?, ?)', reviews)
    conn.commit()
    conn.close()

# Function to initialize the database
def initialize_database():
    create_products_table()
    create_reviews_table()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")
