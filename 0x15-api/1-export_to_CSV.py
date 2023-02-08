#!/usr/bin/python3
# making api call to jsonplaceholder to retrieve information

import sys
from requests import get
import csv

worker_id = sys.argv[1]
endpoint = 'https://jsonplaceholder.typicode.com/users'
url = endpoint + '/' + worker_id

response = get(url)
worker_name = response.json()['username']

todo_endpoint = 'https://jsonplaceholder.typicode.com/todos'
todo_response = get(todo_endpoint)
result = todo_response.json()

worker_id = int(worker_id)

with open('./USER_ID.csv', mode='w') as file:
    for res in result:
        if res['userId'] == worker_id:
            file.write('"{}""{}" "{}" "{}"'.format(res['userId'], worker_name, res['completed'], res['title']))