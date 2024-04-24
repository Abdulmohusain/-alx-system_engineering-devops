#!/usr/bin/python3
"""
Python script that, using this REST API, for
a given employee ID, returns information about
his/her TODO list progress.
"""
import csv
import requests
import sys


def main():
    """main method"""
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_url = url + "users/{}".format(employee_id)
    task_url = user_url + "/todos"

    response_user = requests.get(user_url).json()
    response_task = requests.get(task_url).json()
    username = response_user['username']
    csv_list = []
    for task in response_task:
        inner = []
        inner.append(task['userId'])
        inner.append(username)
        inner.append(task['completed'])
        inner.append(task['title'])
        csv_list.append(inner)

    with open("USER_ID.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_list)


if __name__ == '__main__':
    main()
