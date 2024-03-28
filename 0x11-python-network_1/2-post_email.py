#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with email data.

Usage:
    python 2-post_email.py <url> <email>

Arguments:
    url (str): The URL to which the POST request is sent.
    email (str): The email data to be sent.

Output:
    Prints the response content received from the server after sending the POST request.
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
