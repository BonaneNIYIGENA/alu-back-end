#!/usr/bin/env python3
"""
Export to JSON format
"""
import json
import requests
import sys


def export_to_json(employee_id):
    """
    Exports employee TODO data to JSON format
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get('username')
    
    # Get employee's todos
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()
    
    # Prepare data for JSON
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    
    # Create the JSON structure
    json_data = {str(employee_id): tasks_list}
    
    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)