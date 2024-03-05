#!/usr/bin/python3
"""defines method of subscribers"""
import requests


def top_ten(subreddit):
    """ Queries api to return titles of the first 10 hot postes listed for a given subreddit"""

    info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if info.status_code >= 300:
        print('None')

    else:
        [print(child.get("data").get("title"))
         for child in info.json().get("data").get("children")]
