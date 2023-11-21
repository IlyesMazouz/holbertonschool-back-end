#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    # Get the employee ID from command line arguments
    employee_id = argv[1]

    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch user's tasks
    tasks_url = "{}/todos?userId={}".format(base_url, employee_id)
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    # Count completed tasks
    total_tasks = len(tasks_data)
    completed_tasks = [task for task in tasks_data if task.get("completed")]
    total_completed_tasks = len(completed_tasks)

    # Display the results
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, total_completed_tasks, total_tasks))

    # Display titles of completed tasks
    for task in completed_tasks:
        title = task.get("title")
        print("\t {}".format(title))
