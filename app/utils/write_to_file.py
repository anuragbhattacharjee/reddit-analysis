
def write_to_file(filename, data):

	with open(file_path, "w", newline="") as file:
		mywriter = csv.writer(file)

		for object in data_objects:
			prawScraper = PrawScraper()
			submission = prawScraper.scrape_submission_details(object['id'])
            author = prawScraper.scrape_author_info(object['author'])
			previous_epoch = object['created_utc'] + 1
			count += 1

			print(submission.author)
			try:
					mywriter.writerow([
						submission.id,
						submission.name,
						submission.num_comments,
						submission.score,
						submission.upvote_ratio,
						submission.is_original_content,
						submission.spoiler
					])

				except Exception as err:
					print(f"Couldn't print post: {object['url']}")
					print(traceback.format_exc())
					print(err)
