# Scraping historical tweets about the Bristol Museum

# this is using github code from godkingjay:
# https://github.com/godkingjay/selenium-twitter-scraper

import pandas as pd
from scraper import Twitter_Scraper
import os
import glob
import sys
sys.path.append("/Users/chad/github/museum_twitter")

# Path to save the scraped tweets
OUTPATH = "../data/raw/tweets"

# Inputs needed
EMAIL = input("Enter your email: ")
USERNAME = input("Enter your username: ")
PASSWORD = input("Enter your password: ")

# TODO: just modify the save_to_csv() function to allow naming of the output file
 
# Helper function to rename the last saved file
def rename_last_saved(folder,new_name):
    # Get list of files
    files = os.listdir(folder)
    # Filter out non-CSV files and sort by modification time
    csv_files = [f for f in files if f.endswith('.csv')]
    csv_files.sort(key=lambda f: os.path.getmtime(os.path.join(folder, f)))
    # Get the last saved file
    last_saved_file = csv_files[-1]
    # Rename the file
    os.rename(os.path.join(folder, last_saved_file), os.path.join(folder, new_name))

scraper = Twitter_Scraper(
    mail=EMAIL,
    username=USERNAME,
    password=PASSWORD,
)

# Login to Twitter
scraper.login()

# Scrape tweets from 2014-2015
scraper.scrape_tweets(
    max_tweets=5000,
    scrape_query='"bristol museum" since:2015-04-01 until:2015-12-31',
)
scraper.save_to_csv()
rename_last_saved(folder=OUTPATH, new_name="bristol_tweets_2016.csv")

# ran into an issue with the scraping, so I had toscrape the data in batches in 
# i think the issue is that i just had to wait ~15 minutes to access the older tweets

# read in batches
# batch1 = pd.read_csv("tweets/2024-09-13_12-01-13_tweets_1-854.csv")
# batch2 = pd.read_csv("tweets/2024-09-13_12-11-39_tweets_1-500.csv")
# batch3 = pd.read_csv("tweets/2024-09-13_12-12-37_tweets_1-103.csv")
# assemble as a big dataframe
# df = pd.concat([batch1, batch2, batch3])
# len(df) # 1457

# save the data
# df.to_csv("tweets/bristol_tweets_2015.csv", index=False)

# Scrape tweets from 2016
scraper.scrape_tweets(
    max_tweets=5000,
    scrape_query='"bristol museum" since:2016-01-01 until:2016-12-31',
)
scraper.save_to_csv()
rename_last_saved(folder=OUTPATH, new_name="bristol_tweets_2016.csv")

# Scrape tweets from 2017
scraper.scrape_tweets(
    max_tweets=5000,
    scrape_query='"bristol museum" since:2017-01-01 until:2017-12-31',
)
scraper.save_to_csv()
rename_last_saved(folder=OUTPATH, new_name="bristol_tweets_2017.csv")

# Scrape tweets from 2018
scraper.scrape_tweets(
    max_tweets=5000,
    scrape_query='"bristol museum" since:2018-01-01 until:2018-12-31',
)
scraper.save_to_csv()
rename_last_saved(folder=OUTPATH, new_name="bristol_tweets_2018.csv")

# Scrape tweets from 2019
scraper.scrape_tweets(
    max_tweets=5000,
    scrape_query='"bristol museum" since:2019-01-01 until:2019-02-15',
)
scraper.save_to_csv()
rename_last_saved(folder=OUTPATH, new_name="bristol_tweets_2019.csv")


# Now combine all years into a single file and output the data frame as a CSV file

filenames = glob.glob(OUTPATH + "/bristol*.csv")

dfs = []
for f in filenames:
    df = pd.read_csv(f)
    dfs.append(df)

df_tweets = pd.concat(dfs, ignore_index=True)
df_tweets.to_csv('../data/interim/bristol_tweets_2015_2019.csv', index=False)

