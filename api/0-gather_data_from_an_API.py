#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    employee_name = user_info.get("name")
    task_completed = list(filter(lambda obj: (obj["completed"] is True), todos_info))
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_number_of_tasks))

    for task in task_completed:
        print("\t {}".format(task["title"]))