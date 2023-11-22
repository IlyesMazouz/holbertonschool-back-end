#!/usr/bin/python3
"""
Script to export data to CSV format
"""

import csv
import requests
from sys import argv

def export_to_csv(user_id):
    """
    Export user's tasks to CSV file
    """
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    user_response = requests.get(user_url)
    tasks_response = requests.get(tasks_url)

    user_data = user_response.json()
    tasks_data = tasks_response.json()

    username = user_data.get("username")

    csv_filename = "{}.csv".format(user_id)

    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in tasks_data:
            task_completed_status = task.get("completed")
            task_title = task.get("title")

            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": str(task_completed_status),
                "TASK_TITLE": task_title
            })

    print("Data exported to {}".format(csv_filename))

if __name__ == "__main__":
    export_to_csv(argv[1])
