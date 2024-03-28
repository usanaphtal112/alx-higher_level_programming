#!/usr/bin/python3
"""
This script retrieves the value of the 'X-Request-Id'
header from a given URL using the requests library.

Usage:
    python script_name.py <url>

Arguments:
    url (str): The URL from which to retrieve the 'X-Request-Id' header value.

Output:
    Prints the value of the 'X-Request-Id' header from the response.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
