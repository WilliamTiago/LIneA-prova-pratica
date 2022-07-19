import json
import requests

request = requests.get('https://jsonplaceholder.typicode.com/todos')

if(request.status_code == 200):
    todos  = json.loads(request.content);

    list = []

    for i in range(20):
        register = {
            "id":todos[i]['id'], 
            "title":todos[i]['title']
        }
        list.append(register)

    print(list)
else:
    error = {
        "error": {
        "reason": "error description",
        }
    }
    #print(error)