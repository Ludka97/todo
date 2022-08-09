from django.test import TestCase
import requests

from faker import Faker

fake = Faker()


if __name__ == "__main__":
    base_url = "http://127.0.0.1:8000/"
    response = requests.get(base_url)
    assert response.status_code == 200

    data = {"username": "ludka", "password": "191296"}
    response = requests.post(f"{base_url}/admin/login", data=data)
    assert response.status_code == 200

    print("All tests have passed")