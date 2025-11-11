#!/usr/bin/python3
"""Script to gather data from an API for a given employee ID"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos for the employee
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Calculate completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(completed_tasks)

    # Print the first line
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    # Print completed task titles
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))