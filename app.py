from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Function to create a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('product_reviews.db')
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint to retrieve a list of all products
@app.route('/products', methods=['GET'])
def get_all_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return jsonify([dict(product) for product in products])

# Endpoint to retrieve details of a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    conn.close()
    if product is None:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(dict(product))

# Endpoint to submit a review for a product
@app.route('/products/<int:product_id>/reviews', methods=['POST'])
def submit_review(product_id):
    data = request.json
    rating = data.get('rating')
    comment = data.get('comment')

    if not rating or not comment:
        return jsonify({"error": "Rating and comment are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reviews (product_id, rating, comment) VALUES (?, ?, ?)',
                   (product_id, rating, comment))
    conn.commit()
    conn.close()
    return jsonify({"message": "Review submitted successfully"}), 201

# Endpoint to retrieve reviews for a specific product by ID
@app.route('/products/<int:product_id>/reviews', methods=['GET'])
def get_reviews_for_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reviews WHERE product_id = ?', (product_id,))
    reviews = cursor.fetchall()
    conn.close()
    return jsonify([dict(review) for review in reviews])

if __name__ == '__main__':
    app.run(debug=True)
