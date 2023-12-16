import unittest
import requests
import json
from app import app

class AirbnbAPITestCase(unittest.TestCase):

    API_URL = "http://localhost:5000"

    def setUp(self):
        # Set up test client for application
        self.client = app.test_client(self) 

    def test_get_listings(self):
        # Send GET request and test response
        response = self.client.get("/listings") 
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json)

    def test_get_listing(self):
        # Test getting a specific listing
        response = self.client.get("/listings/1")  
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json["id"], 1)

    def test_create_listing(self):
        # Send POST request and test created listing 
        mock_data = {"title": "New Listing"} 
        response = self.client.post("/listings", 
                        data=json.dumps(mock_data),
                        content_type='application/json') 
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["title"], "New Listing")  

    def test_delete_listing(self):
        # Send DELETE request and check if deleted
        response = self.client.delete("/listings/1")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(response.data), 0) # No data        

if __name__ == "__main__":
    unittest.main()