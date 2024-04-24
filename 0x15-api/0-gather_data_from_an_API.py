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
    tasks_done = [task['title'] for task in response_task if task['completed']]

    print(
        'Employee {} is done with tasks({}/{}):'.format(
            response_user["name"],
            len(tasks_done),
            len(response_task)
        )
    )
    for task in tasks_done:
        print("\t {}".format(task))


if __name__ == '__main__':
    main()
