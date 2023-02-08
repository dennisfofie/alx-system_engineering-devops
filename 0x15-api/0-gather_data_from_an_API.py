#!/usr/bin/python3
# making api call to jsonplaceholder to retrieve information

import sys
from requests import get

worker_id = sys.argv[1]
endpoint = 'https://jsonplaceholder.typicode.com/users'
url = endpoint + '/' + worker_id

response = get(url)
worker_name = response.json()['name']

todo_endpoint = 'https://jsonplaceholder.typicode.com/todos'
todo_response = get(todo_endpoint)
result = todo_response.json()

task_completed = 0
total_task = 0
worker_id = int(worker_id)

for res in result:
    if res['userId'] == worker_id and res['completed'] == True:
        task_completed += 1
    if res['userId'] == worker_id:
        total_task += 1

print('Employee {} is done with tasks({}/{}):'.format(worker_name, task_completed, total_task))

for title in result:
    if title['userId'] == worker_id and title['completed'] == True:
        print('\t {}'.format(title['title']))
