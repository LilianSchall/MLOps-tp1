import requests

data = {
    "size":205.9991686803,
    "nb_rooms": 2,
    "garden": 0,
}

url = "http://0.0.0.0:5000/predict"

response = requests.post(url, json=data)
print("Status Code", response.status_code)
print("JSON Response ", response.json())
