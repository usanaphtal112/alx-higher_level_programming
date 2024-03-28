#!/usr/bin/python3
"""
This script retrieves the content of a web page specified by a URL.

Usage:
    python 3-error_code.py <url>

Arguments:
    url (str): The URL of the web page to retrieve.

Output:
    Prints the content of the web page if the request is successful.
    If the request fails (e.g., HTTP error), prints the error code.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
