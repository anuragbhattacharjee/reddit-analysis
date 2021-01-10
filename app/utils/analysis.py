from utils.get_file_path import get_file_path
import pandas as pd
import matplotlib.pyplot as plt

def analyse(subreddit1, subreddit2):
    file_path = get_file_path(subreddit1)
    
    try:
        subreddit1_df = pd.read_csv(
            file_path, sep="\n",  header=None, names=["id", "name", "num_comments", "score", "upvote_ratio", "is_original_content", "ratio"])

    except Exception as err:
	    print(f"Counldn\'t find file {subreddit1}.csv")

    file_path = get_file_path(subreddit2)

    try:
        subreddit2_df = pd.read_csv(
            file_path, sep="\n",  header=None, names=["id", "name", "num_comments", "score", "upvote_ratio", "is_original_content", "ratio"])

    except Exception as err:
	    print(f"Counldn\'t find file {subreddit2}.csv")

    subreddit1_df.plot()
    subreddit2_df.plot()
