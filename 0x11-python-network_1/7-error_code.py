#!/usr/bin/python3
"""
This script retrieves the content of a web page
specified by a URL using the requests library.

Usage:
    python script_name.py <url>

Arguments:
    url (str): The URL of the web page to retrieve.

Output:
    Prints the content of the web page if the request is successful.
    If the request fails (e.g., HTTP error), prints the error code.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
