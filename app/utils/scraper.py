import time
from datetime import datetime
import requests
from PrawScraper import PrawScraper
from utils.write_to_file import write_to_file

url = "https://api.pushshift.io/reddit/submission/search/?after={}&before={}&subreddit={}&limit=100"

def scrape(subreddit, from_date, to_date):
	count = 0

	# formatting date to UNIX Timestamp
	previous_epoch = from_date = int(time.mktime(datetime.strptime(
		from_date, "%m-%Y").timetuple()))

	to_date = int(time.mktime(datetime.strptime(
		to_date, "%m-%Y").timetuple()))

	data_objects = []
	
	# Keep scraping until any of the conditions expire
	while True:
		if previous_epoch > to_date:
			break

		# Using pushshift to scrape submission id form certain date, 
		# because Reddit has stopped supporting date-based searching. 
		new_url = url.format(previous_epoch, to_date, subreddit)
		
		try:
			json_data = requests.get(new_url).json()
		except Exception as err:
			print(err)
			break

		if 'data' not in json_data:
			break
		if len(json_data['data']) == 0:
			break
		data_objects += json_data['data']

		# pushshift has a rate limit, if we send requests too fast it will start returning error messages
		time.sleep(1)
		post_starting_time = previous_epoch

		for object in data_objects:
			# PrawScraper for getting details data of a reddit submission and author
			prawScraper = PrawScraper()
			
			if object['id']:
				try: 
					submission = prawScraper.scrape_submission_details(object['id'])
					write_to_file(subreddit, [
										submission.id,
										submission.name,
										submission.num_comments,
										submission.score,
										submission.upvote_ratio,
										submission.is_original_content,
										submission.spoiler
									])
				except Exception as err:
					print(f"Counldn\'t find Submission {object['id']}", err)
			
			if object['author'] != "[deleted]":
				try: 
					author = prawScraper.scrape_author_info(object['author'])
					write_to_file(subreddit+"_author", [
                                            author.id,
                                            author.name,
                                            author.link_karma,
                                            author.comment_karma,
                                            author.is_gold
                                        ])
				except Exception as err:
					print(f"Counldn\'t find Author {object['author']}", err)
		
			previous_epoch = object['created_utc'] + 1
			count += 1
			print("Submission data Id {} on {} written in File.".format(object["id"], datetime.fromtimestamp(object["created_utc"]).strftime("%Y-%m-%d")))
		
		print("Scraped data from {} to {}".format(
			datetime.fromtimestamp(post_starting_time).strftime("%Y-%m-%d"), datetime.fromtimestamp(previous_epoch).strftime("%Y-%m-%d")))

	print("Saved {} submissions from {} to {}".format(count, from_date, to_date))
