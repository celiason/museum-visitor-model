# Scraping historical tweets about the Bristol Museum

# NB: this is using github code from godkingjay:
# https://github.com/godkingjay/selenium-twitter-scraper
# It's in 'src/selenium_scraper' in this repo

import pandas as pd
import os
import glob
import sys

from selenium_scraper.twitter_scraper import Twitter_Scraper

# Set where the files will be saved
OUTPATH = "../data/raw/tweets"

# Inputs needed
EMAIL = input("Enter your email: ")
USERNAME = input("Enter your username: ")
PASSWORD = input("Enter your password: ")

# Initialize scraper
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
scraper.save_to_csv(file_path = OUTPATH + "/bristol_tweets_2015.csv")

# Scrape tweets from 2016
scraper.scrape_tweets(
    max_tweets=5000,
    scrape_query='"bristol museum" since:2016-01-01 until:2016-12-31',
)
scraper.save_to_csv(file_path = OUTPATH + "/bristol_tweets_2016.csv")

# Scrape tweets from 2017
scraper.scrape_tweets(
    max_tweets=5000,
    scrape_query='"bristol museum" since:2017-01-01 until:2017-12-31',
)
scraper.save_to_csv(file_path = OUTPATH + "/bristol_tweets_2017.csv")

# Scrape tweets from 2018
scraper.scrape_tweets(
    max_tweets=5000,
    scrape_query='"bristol museum" since:2018-01-01 until:2018-12-31',
)
scraper.save_to_csv(file_path = OUTPATH + "/bristol_tweets_2018.csv")

# Scrape tweets from 2019
scraper.scrape_tweets(
    max_tweets=5000,
    scrape_query='"bristol museum" since:2019-01-01 until:2019-02-15',
)
scraper.save_to_csv(file_path = OUTPATH + "/bristol_tweets_2019.csv")

# TODO: I can probably just run the whole big batch?
# see below
# scraper.scrape_tweets(
#     max_tweets=10000,
#     scrape_query='"bristol museum" since:2014-01-01 until:2019-02-15',
# )
# scraper.save_to_csv(file_path = OUTPATH + "/bristol_tweets_2014_2019.csv")


# Now combine all years into a single file and output the data frame as a CSV file
filenames = glob.glob(OUTPATH + "/bristol*.csv")

dfs = []
for f in filenames:
    df = pd.read_csv(f)
    dfs.append(df)

df_tweets = pd.concat(dfs, ignore_index=True)
df_tweets.to_csv('../data/interim/bristol_tweets_2015_2019.csv', index=False)
