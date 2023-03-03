#!/usr/bin/python3
import requests
"""
number of subscribe users per subreddit
"""


def number_of_subscribers(subreddit):
    """
    return all the subcribers of a specific subreddit
    """

    user_agent = {'User-agent': 'Google Chrome Version 109.0.5414.119'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=user_agent)

    if response:
        return(response.json()['data']['subscribers'])
    else:
        return 0
