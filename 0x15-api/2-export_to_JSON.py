#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    worker_id = sys.argv[1]
    endpoint = 'https://jsonplaceholder.typicode.com/users'
    url = endpoint + '/' + worker_id

    response = requests.get(url)
    worker_name = response.json()['username']

    todo_endpoint = 'https://jsonplaceholder.typicode.com/todos'
    todo_response = requests.get(todo_endpoint)
    result = todo_response.json()

    worker_id = int(worker_id)

    dictionary = {worker_id: []}
    for res in result:
        dictionary[worker_id].append({
            'task': res.get('title'),
            'completed': res.get('completed'),
            'username': worker_name
        })

    with open('{}.json'.format(worker_id), 'w') as file:
        json.dump(dictionary, file)