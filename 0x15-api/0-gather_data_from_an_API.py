#!/usr/bin/python3
# making api call to jsonplaceholder to retrieve information

import sys
from requests import get

if __name__ == '__main__':
    worker_id = sys.argv[1]
    endpoint = 'https://jsonplaceholder.typicode.com/users'
    url = endpoint + '/' + worker_id

    response = get(url)
    worker = response.json()['name']

    todo_endpoint = 'https://jsonplaceholder.typicode.com/todos'
    todo_response = get(todo_endpoint)
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
# done