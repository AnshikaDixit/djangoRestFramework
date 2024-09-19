import requests
import json

URL = "http://127.0.0.1:8000/stuapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}  
    r = requests.get(url=URL, params=data)  # Using GET request with query params
    if r.status_code == 200:
        data = r.json()
        print(data)
    else:
        print(f"Error: {r.status_code}")


def post_data():
    data = {
    'name' : 'Ravi',
    'roll' : 150,
    'city' : 'Kanyakumari'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

def update_data():
    data = {
    'id' : 4,
    'roll' : 114,
    'city' : 'Jaipur'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

def delete_data():
    data = {
    'id' : 4
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

# delete_data()
post_data()
# get_data()  # Call without ID to get all data
# get_data(1)  # Call with ID to get data for a specific student
