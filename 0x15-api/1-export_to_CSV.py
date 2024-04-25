#!/usr/bin/python3
"""
Python script that, using this REST API, for
a given employee ID, returns information about
his/her TODO list progress.
"""
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
    csv_str = ""
    for task in response_task:
        csv_str = csv_str + '"{}"'.format(task['userId'])
        csv_str = csv_str + ',"{}"'.format(username)
        csv_str = csv_str + ',"{}"'.format(task['completed'])
        csv_str = csv_str + ',"{}"\n'.format(task['title'])
    filename = str(response_task[0]['userId']) + ".csv"
    with open(filename, 'w', newline='') as file:
        file.write(csv_str)


if __name__ == '__main__':
    main()
