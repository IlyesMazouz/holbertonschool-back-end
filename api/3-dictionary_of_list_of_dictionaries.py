#!/usr/bin/python3
"""
Script to export data to JSON format
"""

import json
import requests
from sys import argv


def export_to_json():
    """
    Export all users' tasks to JSON file
    """
    base_url = "https://jsonplaceholder.typicode.com"

    users_url = f"{base_url}/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    all_user_tasks = {}

    for user in users_data:
        user_id = str(user.get("id"))
        username = user.get("username")

        tasks_url = f"{base_url}/todos?userId={user_id}"
        tasks_response = requests.get(tasks_url)
        tasks_data = tasks_response.json()

        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in tasks_data
        ]

        all_user_tasks[user_id] = user_tasks

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_user_tasks, json_file)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    export_to_json()
