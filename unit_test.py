import unittest
import json
from app import app

class TestProductReviewSystem(unittest.TestCase):
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

    def test_get_all_products(self):
        # Test retrieving a list of all products
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIsInstance(data, list)

    def test_get_product(self):
        # Test retrieving details of a specific product
        response = self.client.get(f'/products/{self.product_id}')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['id'], self.product_id)

    def test_submit_review(self):
        # Test submitting a review for a product
        response = self.client.post(f'/products/{self.product_id}/reviews', json={"rating": 5, "comment": "Great product!"})
        self.assertEqual(response.status_code, 201)

    def test_get_reviews_for_product(self):
        # Test retrieving reviews for a specific product
        response = self.client.get(f'/products/{self.product_id}/reviews')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
