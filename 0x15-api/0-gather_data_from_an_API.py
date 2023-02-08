#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys

if __name__ == '__main__':
    worker_id = sys.argv[1]
    endpoint = 'https://jsonplaceholder.typicode.com/users'
    url = endpoint + '/' + worker_id

    response = requests.get(url)
    worker = response.json()['name']

    todo_endpoint = 'https://jsonplaceholder.typicode.com/todos'
    todo_response = requests.get(todo_endpoint)
    result = todo_response.json()

    task = 0
    total = 0
    worker_id = int(worker_id)

    for res in result:
        if res.get('userId') == worker_id and res.get('completed') is True:
            task += 1
        if res.get('userId') == worker_id:
            total += 1

    print(f'Employee {worker} is done with tasks({task}/{total}):')

    for title in result:
        if title.get('userId') == worker_id and title.get('completed') is True:
            print('{}'.format(title.get('title')))