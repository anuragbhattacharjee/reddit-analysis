# reddit-analysis

A demo application for scraping reddit posts and make an analysis of them.
This README will guide to install this project and get up and running.

### Reddit Analysis - What is this repository for?

- Scraping reddit posts within a given time period
- Generate CSV with scraped posts with 5 metrics of them
- Compare two sub reddits based on their metrices
- Contributer analysis

### How do I set up?

- git clone https://github.com/anuragbhattacharjee/reddit-analysis.git
- python3.6 -m venv reddit-analysis-venv
- source reddit-analysis-venv/bin/activate
- pip install requirements.txt
- flask run

### Analysis
Please see the notebooks for plotted data analysis. 

I have chosen five metrics for comparing submissions or posts in two subreddits
- "num_comments"        : Number of comments in each post 
- "score"               : Number of upvotes in each post
- "upvote_ratio"        : The percentage of upvotes from all votes on the submission.
- "is_original_content" : Whether or not the submission has been set as original content.
- "spoiler"             : Whether or not the submission has been marked as a spoiler.

I have chosen three metrics for comparing contributors in two subreddits:
- "link_karma"      : The link karma for the Redditor.
- "comment_karma"   : The comment karma for the Redditor.
- "is_gold"         : Number of contributors in each subreddits with Premium status.

### Procedure

I have chosen pushshift for scraping reddit data with given date. As reddit has stopped supporting datebased searching I had to develop a technique to scrape data for exactly certain period. 

I have scraped details data while iterating through the 100 of data that I got from pushshit in each batch. Pushshift sends 100 data at a time and has some limit of requesting their API. 

So to give a aleep time, I have scraped details of the submission and the author meanwhile and saved them in CSV. This also gave me the opportunity to find out the date of the last post. 


### Notable libraries used for accomplishment

- pushshift : for scraping reddit data for a certain time period. 
- praw      : for reddit submission and author details data.
- pandas    : for reading csv data and data analysis.
- jupyter   : for showing data analysis.
- matplotlib: for plotting data.
