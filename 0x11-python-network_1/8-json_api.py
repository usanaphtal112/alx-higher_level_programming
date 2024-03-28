#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with a search query
parameter using the requests library.

Usage:
    python 8-json_api.py [letter]

Arguments:
    letter (str, optional): A single letter to search for.
    If not provided, an empty string is used.

Output:
    Prints the result of the search operation, including the
    user ID and name if a match is found.
    If no result is found, it prints "No result".
    If the response is not a valid JSON, it prints "Not a valid JSON".
"""

import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
