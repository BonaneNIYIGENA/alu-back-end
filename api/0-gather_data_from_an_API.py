#!/usr/bin/python3
"""Script to get TODO list progress for a given employee"""

import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos").json()

    completed_tasks = [t for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))

    for task in completed_tasks:
        print("\t{}".format(task.get("title")))
