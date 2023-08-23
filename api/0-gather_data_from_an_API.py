#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)

    user_response = requests.get(user_url).json()
    tasks_response = requests.get(tasks_url).json()

    employee_name = user_response.get("name")
    total_tasks = len(tasks_response)
    done_tasks = sum(1 for task in tasks_response if task.get("completed"))

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, done_tasks, total_tasks
        )
    )

    for task in tasks_response:
        if task.get("completed"):
            print("\t{}".format(task.get("title")))
