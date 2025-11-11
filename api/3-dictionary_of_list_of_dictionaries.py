#!/usr/bin/python3
"""
Script that exports all employee TODO list data to JSON format.
Uses JSONPlaceholder API to fetch user and todo information.
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_response = requests.get("{}/users".format(base_url))
    users = users_response.json()

    todos_response = requests.get("{}/todos".format(base_url))
    todos = todos_response.json()

    all_employees = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        user_todos = [todo for todo in todos
                      if todo.get("userId") == int(user_id)]

        task_list = []
        for todo in user_todos:
            task_dict = {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            task_list.append(task_dict)

        all_employees[user_id] = task_list

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees, json_file)