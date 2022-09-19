import requests
from django.test import TestCase

# Create your tests here.

url="http://127.0.0.1:8000/accounts/auth"

response = requests.post(url, data={'username' : 'admin', 'password' : 'admin'})

print(response.text)