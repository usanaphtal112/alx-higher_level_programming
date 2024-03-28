#!/usr/bin/python3
"""
This script searches for Star Wars characters using the Star Wars
API (SWAPI) based on the provided search query.

Usage:
    python 9-starwars.py <search_query>

Arguments:
    search_query (str): The name of the Star Wars character to search for.

Output:
    Prints the number of results found and the names of
    the characters matching the search query.
"""

import sys
import requests


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    params = {"search": sys.argv[1]}
    results = requests.get(url, params=params).json()

    print("Number of results: {}".format(results.get("count")))
    [print(r.get("name")) for r in results.get("results")]
