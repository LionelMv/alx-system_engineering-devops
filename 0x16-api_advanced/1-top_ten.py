#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Return top ten titles for a given subreddit
    Return None if invalid subreddit given
    """

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'ubuntu_api_advanced_v1.0'}

    # Make the API request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    response_data = response.json()
    # print(response_data)
    hot_ten = response_data["data"]["children"]
    for data in hot_ten:
        title = data["data"]["title"]
        print(title)
