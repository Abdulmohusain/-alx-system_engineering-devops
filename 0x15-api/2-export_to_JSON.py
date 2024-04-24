#!/usr/bin/python3
"""
Python script that, using this REST API, for
a given employee ID, returns information about
his/her TODO list progress.
"""
import json
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
    dict_data = {response_task[0]['userId']: []}
    for task in response_task:
        inner_dict = {}
        inner_dict["task"] = task["title"]
        inner_dict["completed"] = task["completed"]
        inner_dict["username"] = username
        dict_data[response_task[0]['userId']].append(inner_dict)

    file_name = str(response_task[0]['userId']) + ".json"
    with open(file_name, 'w') as file:
        json.dump(dict_data, file)


if __name__ == '__main__':
    main()
