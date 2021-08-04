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

def convert_list_to_dict(entries, current, questions, answers):
    ''' '''



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

    # find text
    try: 
        soup = BeautifulSoup(page.text, features='lxml')
        entries = soup.find_all('p')
    
    except:
        raise   

    questions_idx = [i for i, elem in enumerate(e.getText() for e in entries) if elem.startswith('Q:')]
    logger.debug(questions_idx)

    # parse outputs, format into a csv with each row as Q/A
    df = pd.DataFrame({'question': [], 'answer': []})
    for index, original_index in enumerate(questions_idx):
        current_question = entries[original_index].getText()
        start = original_index+1
        if index+1 < len(questions_idx):
            next_ = questions_idx[index+1] 
        else:
            next_ = questions_idx[index]
        logger.debug(f'{start}, {next_}')
        current_answer_list = entries[start:next_]
        current_answer = '\n\n'.join(t.getText() for t in current_answer_list)
        df = df.append({
            'question': current_question,
            'answer': current_answer,
        }, ignore_index=True)

    logger.info(df)


        
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))