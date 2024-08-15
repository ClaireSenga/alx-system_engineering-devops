#!/usr/bin/python3
"""
A script that queries subscribers on given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total num of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; YourScriptName/1.0)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    else:
        # Return 0 if the subreddit is invalid or other errors occur
        return 0
