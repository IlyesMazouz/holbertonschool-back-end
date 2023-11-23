#!/usr/bin/python3
"""
Gather data about employees TODO and export to JSON
"""

import json
import requests
from collections import defaultdict

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def fetch_user_info():
    """ Fetch user info """
    correct_output = defaultdict(list)

    response = requests.get(todos_url).json()
    for item in response:
        url = users_url + str(item['userId'])
        usr_resp = requests.get(url).json()
        correct_output[item['userId']].append({
            'username': usr_resp[0]['username'],
            'completed': item['completed'],
            'task': item['title']
        })

    return correct_output


def export_to_json(data, filename='todo_all_employees.json'):
    """ Export data to JSON """
    with open(filename, 'w') as f:
        json.dump(data, f)


def check_student_output():
    """ Check student JSON output """
    with open('todo_all_employees.json', 'r') as f:
        student_output = json.load(f)

    correct_output = fetch_user_info()

    all_users_exist = all(str(correct_key) in student_output
                          for correct_key in correct_output.keys())

    if all_users_exist:
        print("All users found: OK")
    else:
        print("Some users are missing in the output")

    all_tasks_correct = all(student_output[str(correct_key)] == correct_entry
                            for correct_key, correct_entry in correct_output.items())

    if all_tasks_correct:
        print("User ID and Tasks output: OK")
    else:
        print("Tasks are incorrect for some User IDs")


if __name__ == "__main__":
    export_to_json(fetch_user_info())
    check_student_output()
