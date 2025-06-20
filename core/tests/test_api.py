from django.test import TestCase
from ninja.testing import TestClient
from core.api import router

class HelloWorldTest(TestCase):
  def test_hello_endpoint(self):
    client = TestClient(router)
    response = client.get("/hello")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(), {"msg": "Hello World"})