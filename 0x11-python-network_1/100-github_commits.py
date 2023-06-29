#!/usr/bin/python3
"""list 10 commits"""
if __name__ == '__main__':
    import requests
    import sys

    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    headers = {
            
            }
    res = requests.get(url, headers=headers)
    commits = res.json
