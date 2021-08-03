#!/usr/bin/env python3

"""A simple python script template.
"""

import argparse
import logging
import os
import pandas as pd
import requests
import sys
import urllib

from bs4 import BeautifulSoup 

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
    parser.add_argument('url', help="Input url to scrape")
    parser.add_argument('-d', '--debug', help="DEBUG flag", dest='debug', action='store_true')
    parser.set_defaults(debug=False)
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)
    URL = args.url
    DEBUG = args.debug

    # set up logger
    if DEBUG:
        logger = logging.getLogger(logging.basicConfig(level=logging.DEBUG))
        logger.debug('*** Debug mode ***')
    else:
        logger = logging.getLogger(logging.basicConfig(level=logging.INFO))
    
    logger.debug(args)

    # get page
    logger.info('Retrieving page...')
    page = get_url(URL)
    logger.info(f'Page received.')
    logger.debug(page.text)




    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))