#!/usr/bin/python3
"""
Python script that uses a REST API to return information about
an employee's TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    employee_name = user_data.get("name")

    # Fetch user's todo list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed") is True]
    done_count = len(done_tasks)

    # Display progress
    print(f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
