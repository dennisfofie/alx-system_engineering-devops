#!/usr/bin/python3
"""
number of subscribe users per subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    return all the subcribers of a specific subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    user_agent = {'User-agent': 'Google Chrome Version 109.0.5414.119'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=user_agent)

    if response:
        return(response.json()['data']['subscribers'])
    else:
        return 0
