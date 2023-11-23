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

    error = False
    for correct_key, correct_entry in fetch_user_info().items():
        flag = 0
        for student_key, student_entry in student_output.items():
            if str(correct_key) == str(student_key):
                flag = 1
                message = "User ID {} Tasks: Incorrect".format(
                    str(correct_key))
                print(message)
                error = True
        if flag == 0:
            message = "User ID {}: Not found".format(str(correct_key))
            print(message)
            error = True

    if not error:
        print("User ID and Tasks output: OK")


if __name__ == "__main__":
    export_to_json(fetch_user_info())
    check_student_output()
