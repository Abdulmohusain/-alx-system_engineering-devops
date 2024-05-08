#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""

    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent':
        'script:subscriber_counter_v0.1 by /u/abdulmohusain'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        suscribers = response.json()['data']['subscribers']
        return suscribers
    else:
        return 0
