#!/usr/bin/python3
"""
Script to export data to JSON format
"""

import json
import requests
from sys import argv


def export_to_json(user_id):
    """
    Export user's tasks to JSON file
    """
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(user_id)
    )
    tasks_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(user_id)
    )

    user_response = requests.get(user_url)
    tasks_response = requests.get(tasks_url)

    user_data = user_response.json()
    tasks_data = tasks_response.json()

    username = user_data.get("username")
    json_filename = "{}.json".format(user_id)

    if isinstance(tasks_data, list) and all(isinstance(task, dict) for task in tasks_data):
        user_tasks = {
            str(user_id): [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                }
                for task in tasks_data
            ]
        }

        with open(json_filename, mode='w') as json_file:
            json.dump(user_tasks, json_file)

        print("Data exported to {}".format(json_filename))
    else:
        print("Error: Invalid data format from tasks API")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <user_id>".format(argv[0]))
    else:
        export_to_json(argv[1])
