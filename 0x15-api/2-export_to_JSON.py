#!/usr/bin/python3
"""extend your python script to export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id)).json()
    name = user.get('name')
    tasks = []
    for task in todos:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = name
        tasks.append(task_dict)
    dictobj = {}
    dictobj[user_id] = tasks
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(dictobj, jsonfile)
