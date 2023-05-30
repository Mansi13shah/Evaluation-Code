import requests

url = 'http://192.168.1.94:5001/joinDataframes'

data = {
    "dataframe1": [
        {
            "id": 1,
            "name": "John"
        },
        {
            "id": 2,
            "name": "Jane"
        }
    ],
    "dataframe2": [
        {
            "id": 1,
            "age": 30
        },
        {
            "id": 3,
            "age": 25
        }
    ]
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)

print(response.json())
