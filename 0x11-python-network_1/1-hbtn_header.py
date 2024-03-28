#!/usr/bin/python3
"""
This script retrieves the value of the 'X-Request-Id' header from a given URL.

Usage:
    python 1-hbtn_header.py <url>

Arguments:
    url (str): The URL from which to retrieve the 'X-Request-Id' header value.

Output:
    Prints the value of the 'X-Request-Id' header from the response.
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
