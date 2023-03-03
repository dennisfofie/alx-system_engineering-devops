#!/usr/bin/python3
"""
getting top ten title from a subredddit
"""
import requests


def top_ten(subreddit):
    """
    top ten title of hot reddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    user_agent = {'User-agent': 'Google Chrome Version 109.0.5414.119'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    response = requests.get(url, headers=user_agent)

    i = 0
    while i < 10:

        try:
            result = response.json()['data']['children'][i]['data']['title']

            if result:
                print(result)
                i = i+1
        except Exception as e:
            return

    print('None')
