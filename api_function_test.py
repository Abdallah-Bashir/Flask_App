import unittest
import requests

class TestAPIFunctions(unittest.TestCase):
    base_url = "http://localhost:5000"  # Update with the base URL of your API

    def test_add_product(self):
        # Test adding a new product to the database
        payload = {"name": "New Product", "price": 9.99}
        response = requests.post(f"{self.base_url}/products", json=payload)
        self.assertEqual(response.status_code, 201)  # Check if product is added successfully

    def test_get_product(self):
        # Test retrieving details of a specific product
        product_id = 1  # Specify the ID of the product to retrieve
        response = requests.get(f"{self.base_url}/products/{product_id}")
        self.assertEqual(response.status_code, 200)  # Check if request is successful

    def test_submit_review(self):
        # Test submitting a review for a product
        product_id = 1  # Specify the ID of the product to submit a review for
        payload = {"rating": 4, "comment": "Great product!"}
        response = requests.post(f"{self.base_url}/products/{product_id}/reviews", json=payload)
        self.assertEqual(response.status_code, 201)  # Check if review is submitted successfully

    def test_get_reviews_for_product(self):
        # Test retrieving reviews for a specific product
        product_id = 1  # Specify the ID of the product to retrieve reviews for
        response = requests.get(f"{self.base_url}/products/{product_id}/reviews")
        self.assertEqual(response.status_code, 200)  # Check if request is successful

if __name__ == "__main__":
    unittest.main()
