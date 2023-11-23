#!/usr/bin/python3
"""
Exports data in the JSON format.
"""

import json
import requests
from sys import argv


def export_to_json():
    """
    Exports tasks data to JSON format.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    tasks = response.json()

    if tasks:
        employee_tasks = {}
        for task in tasks:
            user_id = task.get("userId")
            task_info = {"username": "USERNAME", "task": task.get("title"), "completed": task.get("completed")}

            if user_id in employee_tasks:
                employee_tasks[user_id].append(task_info)
            else:
                employee_tasks[user_id] = [task_info]

    if employee_tasks:
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(employee_tasks, json_file)


if __name__ == "__main__":
    export_to_json()
