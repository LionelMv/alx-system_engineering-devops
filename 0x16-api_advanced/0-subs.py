#!/usr/bin/python3
"""
Module contains function that queries the Reddit API
for number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return number of subscribers for a given subreddit
    Return 0 if invalid subreddit given
    """
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'ubuntu_api_advanced_v1.0'}

    # Make the API request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
