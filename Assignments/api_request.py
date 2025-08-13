import requests

url = "http://localhost:8000/calculator"
payload = {"a": 5.1, "b": 0,"operation":'divide'}  # Replace with your data

response = requests.post(url, json=payload)  # Use .get() for GET requests

a = response.json()  # Safely get the JSON response
# print(a.get('detail', None)[0]['msg'] ) # Safely get 'result' key, if it exists
print("Status code:", response.status_code)
print("Response JSON:", a)

