import praw
from datetime import datetime
import time
from configs.Credentials import API

class PrawScraper():

    def __init__(self):
        self.reddit = praw.Reddit(
            client_id="8SyO1l_vzgOD9w",
            client_secret="lKrCHftWzMtib_ZWMjwEIyF-GuKSZQ",
            user_agent="scraper-app"
        )

    def scrape_submission_details(self, submission_id):
        submission = self.reddit.submission(id=submission_id)
        return submission

    def scrape_author_info(self, author_name):
        author = self.reddit.redditor(author_name)
        return author

        
