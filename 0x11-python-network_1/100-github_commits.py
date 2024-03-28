#!/usr/bin/python3
"""
This script retrieves the latest commits (up to 10) from a
specified GitHub repository using the GitHub API.

Usage:
    python 100-github_commits.py <owner> <repo_name>

Arguments:
    owner (str): The username or organization name that owns the GitHub repo.
    repo_name (str): The name of the GitHub repository.

Output:
    Prints the SHA and author name of the latest commits (up to 10).
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print(
                "{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name"),
                )
            )
    except IndexError:
        pass
