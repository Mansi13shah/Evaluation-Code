# Evaluation-Code
A Flask-based API server for joining two dataframes.
# Overview
This project provides a web API endpoint that allows users to join two dataframes using an inner join operation. It aims to simplify the process of dataframe joining by providing a convenient and efficient solution through a RESTful API.

Key features and goals of the project include:
Joining two dataframes based on a common column using an inner join.
Returning the resulting joined dataframe as the API response.
Error handling for invalid input data or join operation failures.
# Project Setup
To set up and run the project locally, follow these steps:

Prerequisites:

Python 3.x installed on your system.
Flask library installed (use pip install flask to install).

Clone the repository:

$ git clone https://github.com/Mansi13shah/Evaluation-Code.git

Navigate to the project directory:

cd repository

Install project dependencies:

pip install -r requirements.txt

Run the API server:

python -m test –config constants.ini

The API server should now be running on the host port mentioned in the constants.ini

# Usage
To join two dataframes using the API, follow these steps:

Prepare the input dataframes in JSON format. Each dataframe should be an array of objects, where each object represents a row in the dataframe.

Send a POST request to the /joinDataframes endpoint with the input dataframes. 

For example:

```
import requests

url = 'http://192.168.1.94:5001/joinDataframes'

payload = {
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


```

The API will perform the join operation on the specified common column and return the resulting joined dataframe as the response.

# Testing the API Endpoint using cURL
```
curl -X POST -H "Content-Type: application/json" -d '{
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
}' http://192.168.1.94:5001/joinDataframes
```



