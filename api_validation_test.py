import unittest
import requests

class TestAPIValidation(unittest.TestCase):
    base_url = "http://localhost:5000"  # Update with the base URL of your API

    def test_submit_review(self):
        # Define the payload for the review
        review_data = {
            "rating": 4,  # Specify the rating for the review
            "comment": "Great product!"  # Specify the comment for the review
        }

        # Send a POST request to submit a review for a specific product
        product_id = 1  # Specify the ID of the product
        response = requests.post(f"{self.base_url}/products/{product_id}/reviews", json=review_data)
        
        # Assert that the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Assert that the response contains JSON data
        self.assertTrue(response.headers.get("content-type").startswith("application/json"))

        # Add more assertions to validate the structure and content of the response data as needed

if __name__ == "__main__":
    unittest.main()
