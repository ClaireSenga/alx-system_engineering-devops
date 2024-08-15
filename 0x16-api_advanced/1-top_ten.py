#!/usr/bin/python3
"""
This module contains the function top_ten.
"""

import requests


def top_ten(subreddit):
    """
    Prints titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is invalid or there's an error, prints None.
    """
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; YourScriptName/1.0)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print(None)
        else:
            for post in posts:
                print(post.get('data', {}).get('title'))
    except (requests.RequestException, ValueError):
        print(None)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
