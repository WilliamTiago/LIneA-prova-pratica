import json
import requests

request = requests.get('https://jsonplaceholder.typicode.com/todos')
todos   = json.loads(request.content);

list = []

for i in range(20):
    list.append(todos[i])

print(list)