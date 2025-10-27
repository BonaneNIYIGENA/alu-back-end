#!/usr/bin/env python3
"""
Dictionary of list of dictionaries for all employees
"""
import json
import requests


def export_all_to_json():
    """
    Exports all employees' TODO data to a single JSON file
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get all users
    users_response = requests.get(f"{base_url}/users")
    users_data = users_response.json()
    
    # Get all todos
    todos_response = requests.get(f"{base_url}/todos")
    todos_data = todos_response.json()
    
    # Create a dictionary to store all data
    all_data = {}
    
    # Organize todos by user ID
    for user in users_data:
        user_id = str(user.get('id'))
        username = user.get('username')
        
        # Filter todos for this user
        user_todos = [task for task in todos_data if task.get('userId') == user.get('id')]
        
        # Create the list of tasks for this user
        tasks_list = []
        for task in user_todos:
            tasks_list.append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            })
        
        # Add to the main dictionary
        all_data[user_id] = tasks_list
    
    # Write to JSON file
    filename = "todo_all_employees.json"
    with open(filename, 'w') as jsonfile:
        json.dump(all_data, jsonfile)


if __name__ == "__main__":
    try:
        export_all_to_json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)