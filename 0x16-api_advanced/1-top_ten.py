#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    url_link = "https://oauth.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit
    )
    headers = {'User-Agent':
               'script:subscriber_counter_v0.1 by /u/abdulmohusain'
               }
    response = requests.get(url_link, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        item = response.json()['data']['children']
        all_titles = [
            titl['data']['title']
            for titl in item
            if titl['kind'] == 't3'
        ]
        for titl in all_titles:
            print(titl)
    else:
        return None
