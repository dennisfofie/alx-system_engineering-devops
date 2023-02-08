#!/usr/bin/python3
# making api call to jsonplaceholder to retrieve information

import sys
from requests import get
import json

worker_id = sys.argv[1]
endpoint = 'https://jsonplaceholder.typicode.com/users'
url = endpoint + '/' + worker_id

response = get(url)
worker_name = response.json()['username']

todo_endpoint = 'https://jsonplaceholder.typicode.com/todos'
todo_response = get(todo_endpoint)
result = todo_response.json()

worker_id = int(worker_id)

dictionary = {worker_id: []}
for res in result:
    dictionary[worker_id].append({
        'task': res['title'],
        'completed': res['completed'],
        'username': worker_name
    })
with open('{}.json'.format(worker_id), 'w') as file:
    json.dump(dictionary, file)