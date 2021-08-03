#!/usr/bin/env python3

"""A simple python script template.
"""

import os
import sys
import argparse

import urllib
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_url(url):
    '''wget a url '''
    try:
        return requests.get(url)
    except requests.exception.RequestException as e:
        raise SystemExit(e)


def main(arguments):

    # default parse args
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('url', help="Input url to scrape", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    print(args)

    # logic
    # get the page
    page = get_url(args['url'])

    # parse the text

    # create a dataframe



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))