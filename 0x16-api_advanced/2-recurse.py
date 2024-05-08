#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit. If no
results are found for the given subreddit, the function
should return None.
"""
import requests


def recurse(subreddit, hot_list=[], count=0, af=None):
    """
    queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function
    should return None.
    """
    url = "https://oauth.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent':
               'script:subscriber_counter_v0.1 by /u/abdulmohusain'
               }
    resp = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
        params={"count": count, "after": af}
    )

    if resp.status_code == 200:
        if resp.status_code == 200:
            h = hot_list + ([
                obj['data']['title']
                for obj in resp.json()['data']['children']
                ])
        resp_json = resp.json()
        if not resp_json.get("data").get("after"):
            return h
        return recurse(
            subreddit,
            hot_list,
            resp_json.get('data').get('count'),
            resp_json['data']['after']
        )
    else:
        return None
