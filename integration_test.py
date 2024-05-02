import unittest
import json
from app import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Set up test client
        self.client = app.test_client()
        # Create a test product in the database
        self.product_id = self.create_test_product()

    def create_test_product(self):
        # Create a test product in the database and return its ID
        response = self.client.post('/products', json={"name": "Test Product", "price": 9.99})
        data = response.json
        return data['id']

    def tearDown(self):
        # Clean up test product from the database
        self.client.delete(f'/products/{self.product_id}')


    def test_add_product_and_get_product_details(self):
        # Test adding a product to the database and then retrieving its details
        # Add a product to the database
        response = self.client.post('/products', json={"name": "New Product", "price": 9.99})
        self.assertEqual(response.status_code, 201)  # Check if product is added successfully

        # Retrieve details of the newly added product
        response = self.client.get(f'/products/{self.product_id}')
        self.assertEqual(response.status_code, 200)  # Check if request is successful

        # Check if the retrieved product details match the added product
        data = response.json
        self.assertEqual(data['name'], "New Product")

    def test_add_review_to_product(self):
        # Test adding a review to a product
        review_data = {"rating": 5, "comment": "Great product!"}
        response = self.client.post(f'/products/{self.product_id}/reviews', json=review_data)
        self.assertEqual(response.status_code, 201)  # Check if review is added successfully

if __name__ == '__main__':
    unittest.main()
