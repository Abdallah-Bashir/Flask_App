from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_product(self):
        product_id = 1  # Specify the ID of the product you want to view
        self.client.get(f'/products/{product_id}')

    @task
    def submit_review(self):
        product_id = 1  # Specify the ID of the product for which you want to submit a review
        review_data = {"rating": 5, "comment": "Great product!"}
        self.client.post(f'/products/{product_id}/reviews', json=review_data)

    # Add more tasks to simulate different user behaviors

