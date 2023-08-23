#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


def gather_employee_todo_list(employee_id):
    """
    Gathers employee TODO list progress using a REST API
    """

    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    todo_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    )

    try:
        employee_name = user_response.json().get("name")
        tasks = todo_response.json()

        total_tasks = len(tasks)
        done_tasks = sum(task.get("completed") for task in tasks)
    except Exception as e:
        print("Error: {}".format(e))
        return

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, done_tasks, total_tasks
        )
    )

    for task in tasks:
        if task.get("completed"):
            print("\t{}".format(task.get("title")))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    gather_employee_todo_list(employee_id)
