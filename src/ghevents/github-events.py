#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    "Download GitHub event data from URL, convert from JSON to Python object"
    json_text = requests.get(url).text
    events = json.loads(json_text)
    return events

def print_events(events, n=5):
    "Print the type and repository name for the first n GitHub events"
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

def main():
    "Print GHUSER and URL and "
    print(GHUSER)
    print(url)
    list = retrieve_events(url)
    print_events(list)

if __name__ == "__main__":
    main()

