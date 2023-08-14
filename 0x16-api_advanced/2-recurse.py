#!/usr/bin/python3
"""
This module defines a function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="None"):
    """
    Return all hot articles for a given subreddit
    Return None if invalid subreddit given
    """
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'ubuntu_api_advanced_v1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f"?after={after}"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 400:
        return None

    r_data = response.json()
    # print(r_data)
    try:
        results = r_data['data']['children']
        # results = data.get("data", {}).get("children", [])
    except KeyError:
        return None

    for entry in results:
        # hot_list.append(entry.get('data').get('title'))
        hot_list.append(entry["data"]["title"])

    next_after = r_data.get('data').get('after')
    if not next_after:
        return hot_list
    return recurse(subreddit, hot_list, next_after)
