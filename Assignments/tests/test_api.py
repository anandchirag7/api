import requests

BASE_URL = "http://127.0.0.1:8000"

def test_create_product():
    data = {"sku": "SKU123", "name": "Test Product", "price": 10.5, "stock": 100}
    r = requests.post(f"{BASE_URL}/products/", json=data)
    print(r.status_code, r.json())

def test_create_order():
    data = {"product_id": 1, "quantity": 2, "status": "pending"}
    r = requests.post(f"{BASE_URL}/orders/", json=data)
    print(r.status_code, r.json())

if __name__ == "__main__":
    test_create_product()
    test_create_order()
