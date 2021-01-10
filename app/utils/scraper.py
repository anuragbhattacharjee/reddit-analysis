import time
import traceback
from datetime import datetime
import requests
import csv
import os
from PrawScraper import PrawScraper
from utils.write_to_file import write_to_file

url = "https://api.pushshift.io/reddit/submission/search/?after={}&before={}&subreddit={}&limit=100"

def scrape(subreddit, from_date, to_date):
	count = 0
	previous_epoch = from_date = int(time.mktime(datetime.strptime(
		from_date, "%m-%Y").timetuple()))

	to_date = int(time.mktime(datetime.strptime(
		to_date, "%m-%Y").timetuple()))

	data_objects = []
	
	while True:
		if previous_epoch > to_date:
			break
		new_url = url.format(previous_epoch, to_date, subreddit)
		json_data = requests.get(new_url).json()
		print(previous_epoch)
		print(to_date)
		print("Count ", count)
		
		if 'data' not in json_data:
			break
		if len(json_data['data']) == 0:
			break
		data_objects += json_data['data']

		# pushshift has a rate limit, if we send requests too fast it will start returning error messages
		time.sleep(1)

		for object in data_objects:
			prawScraper = PrawScraper()
			submission = prawScraper.scrape_submission_details(object['id'])
			author = prawScraper.scrape_author_info(object['author'])
			
			write_to_file(subreddit, [
                            submission.id,
                            submission.name,
                            submission.num_comments,
                            submission.score,
                            submission.upvote_ratio,
                            submission.is_original_content,
                            submission.spoiler
                        ])

			write_to_file(subreddit+"_author", [
				author.id,
				author.name,
				author.link_karma,
				author.comment_karma,
				author.is_gold
			])

			previous_epoch = object['created_utc'] + 1
			count += 1

	print("Saved {} submissions from {} to {}".format(count, from_date, to_date)
