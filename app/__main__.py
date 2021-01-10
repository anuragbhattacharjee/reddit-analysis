import json
import logging
import os
from utils.scraper import scrape
from utils.analysis import analyse

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(
                            os.getpid()),
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[logging.StreamHandler()])

    logger = logging.getLogger()

    logger.info(f'Starting app...')

    print(f'Please type the name of the subreddits you want to scrape and compare.')

    subreddit1 = input("First Subreddit: ")
    subreddit2 = input("Second subreddit: ")

    print(f"For seeing analysis press 1, for scraping press 2")

    flag = int(input("Key: "))

    if flag == 1:
        analyse(subreddit1, subreddit2)
    elif flag == 2:
        print(
            f'Please type the from and to date in MM-YYYY format.')
        from_date = input("From: ")
        to_date = input("To: ")

        logger.info(
            f'Scraping data from r/{subreddit1} and r/{subreddit2}')
        
        scrape(subreddit1, from_date, to_date)
        scrape(subreddit2, from_date, to_date)
    else:
        logger.error("Invalid Key!")    



    
