#!/usr/bin/python3
"""
Script that exports employee TODO list data to JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos"

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos data
    todos_response = requests.get(todos_url, params={"userId": user_id})
    if todos_response.status_code != 200:
        sys.exit(1)
    todos_data = todos_response.json()

    # Format data according to requirements
    tasks_list = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)

    # Create the final JSON structure
    json_data = {str(user_id): tasks_list}

    # Write to file
    filename = f"{user_id}.json"
    with open(filename, mode='w') as json_file:
        json.dump(json_data, json_file)