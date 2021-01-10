import json
import logging
import os
from utils.scraper import scrape


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(
                            os.getpid()),
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[logging.StreamHandler()])

    logger = logging.getLogger()

    logger.info(f'Starting app...')

    # logger.info(
    #     f'Please type the name of the subreddits you want to scrape and compare.')
    # subreddit1 = input("First Subreddit: ")
    # subreddit2 = input("Second subreddit: ")

    # logger.info(
    #     f'Please type the from and to date in MM-YYYY format.')
    # from_date = input("From: ")
    # to_date = input("To: ")

    # logger.info(
    #     f'Scraping data from r/{subreddit1} and r/{subreddit2}')

    # scrape(subreddit1, from_date, to_date)
    # scrape("emacs", "01-2020", "03-2020")
    scrape("emacs", "01-2020", "03-2020")
    
