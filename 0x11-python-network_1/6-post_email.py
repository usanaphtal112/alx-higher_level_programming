#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with email data using the requests library.

Usage:
    python script_name.py <url> <email>

Arguments:
    url (str): The URL to which the POST request is sent.
    email (str): The email data to be sent.

Output:
    Prints the response content received from the server after sending the POST request.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
