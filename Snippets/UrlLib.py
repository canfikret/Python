#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:

    python urllib.py <URL>
"""
import sys
from urllib.request import urlopen

def fetch_url(url):
    """Fetch a list of words from a URL.

    Args:
        url:The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    story_words = []
    
    with urlopen(url) as story:
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    return story_words

def print_items(items):
    """Print items one per line.

    Args:
       list of iterable items.
    """
    for item in items:
        print(item)

def main(url):
    """Print each word from a text document from a URL.

    Args:
        url:The URL of a UTF-8 text document.
    """
    words = fetch_url(url)
    print_items(words)


if __name__ == "__main__":
    # test with static URL
    url = 'http://sixty-north.com/c/t.txt'
    #url = sys.argv[1] 
    main(url)
