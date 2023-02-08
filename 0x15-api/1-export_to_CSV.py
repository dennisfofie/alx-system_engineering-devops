#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys

if __name__ == __main__:
    worker_id = sys.argv[1]
    endpoint = 'https://jsonplaceholder.typicode.com/users'
    url = endpoint + '/' + worker_id

    response = requests.get(url)
    m = response.json()['username']

    todo_endpoint = 'https://jsonplaceholder.typicode.com/todos'
    todo_response = requests.get(todo_endpoint)
    result = todo_response.json()

    worker_id = int(worker_id)

    with open('./USER_ID.csv', mode='w') as file:
        for r in result:
            id = r.get('userId')
            done = r.get('completed')
            t = r.get('title')
            if id == worker_id:
                file.write(f'"{id}""{m}" "{done}" "{t}"')