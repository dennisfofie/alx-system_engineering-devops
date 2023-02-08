#!/usr/bin/python3
# making api call to jsonplaceholder to retrieve information

import sys
from requests import get
import csv

if __name__ == __main__:
    worker_id = sys.argv[1]
    endpoint = 'https://jsonplaceholder.typicode.com/users'
    url = endpoint + '/' + worker_id

    response = get(url)
    m = response.json()['username']

    todo_endpoint = 'https://jsonplaceholder.typicode.com/todos'
    todo_response = get(todo_endpoint)
    result = todo_response.json()

    worker_id = int(worker_id)

    with open('./USER_ID.csv', mode='w') as file:
        for r in result:
            id = r.get('userId')
            done = r.get('completed')
            t = r.get('title')
            if id == worker_id:
                file.write(f'"{id}""{m}" "{done}" "{t}"')