#!/usr/bin/python3
"""
This script retrieves the user ID from the GitHub
API using HTTP basic authentication.

Usage:
    python 10-my_github.py <username> <password>

Arguments:
    username (str): The GitHub username.
    password (str): The GitHub password or personal access token.

Output:
    Prints the user ID of the authenticated user.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
