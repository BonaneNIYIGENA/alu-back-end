#!/usr/bin/python3
# Script that uses a REST API to return information about an employee's todo list progress

import requests
import sys

if __name__ == "__main__":
    # Check if an employee ID is provided
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Extract employee name
    employee_name = user_data.get("name")

    # Get todos for that user
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Compute total and completed tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")