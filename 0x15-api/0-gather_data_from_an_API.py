#!/usr/bin/python3
"""returns information about his/her todo list progress"""
import requests
from sys import argv

if __name__ == '__main__':

    user_id = argv[1]
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(user_id)).json()
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)).json()
    total_tasks = []
    for task in todos:
        if task.get('completed') is True:
            total_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          len(total_tasks), len(todos)))
    print("\n".join("\t {}".format(task) for task in total_tasks))
