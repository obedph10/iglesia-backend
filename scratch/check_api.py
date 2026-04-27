import requests

try:
    response = requests.get('http://localhost/api/contact/settings/')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
