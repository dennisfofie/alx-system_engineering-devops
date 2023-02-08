from requests import get
import sys

response = get('https://jsonplaceholder.typicode.com/users/2')
url = 'https://jsonplaceholder.typicode.com/todos/'
todo = get(url)
result = response.json()['name']
tomark = todo.json()

worker_id = int(sys.argv[1])

count = 0
another_count = 0

for i in tomark:
    if i['userId'] == worker_id and i['completed'] == True:
        count += 1
    if i['userId'] == worker_id:
        another_count += 1

print(f'Employee {result} is done with tasks({count}/{another_count}):')

for title in tomark:
    if title['userId'] == worker_id and title['completed'] == True:
        print(title['title'])
