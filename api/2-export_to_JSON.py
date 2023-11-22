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


if __name__ == "__main__":
    export_to_json(argv[1])
