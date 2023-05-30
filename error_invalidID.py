import requests

url = 'http://192.168.1.94:5001/joinDataframes'

payload = {
    "dataframe1": [
        {
            "name": "John"
        },
        {
            "name": "Jane"
        }
    ],
    "dataframe2": [
        {
            "id": 1,
            "age": 25
        },
        {
            "id": 2,
            "age": 30
        }
    ],
    "joinType": "leftJoin"
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())
