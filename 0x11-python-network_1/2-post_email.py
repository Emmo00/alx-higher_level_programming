#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    with urllib.request.urlopen(url) as response:
