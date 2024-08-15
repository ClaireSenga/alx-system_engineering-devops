#!/usr/bin/python3
"""Contains a recurse function."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on the given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None
    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])
    after = data.get("after")

    if not children:
        return hot_list if hot_list else None

    for child in children:
        hot_list.append(child.get("data", {}).get("title"))

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
