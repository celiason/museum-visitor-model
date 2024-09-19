# Scraping historical tweets about the Bristol Museum
# this is using github code from godkingjay:
# https://github.com/godkingjay/selenium-twitter-scraper

import sys
import os
import glob
import pandas as pd

sys.path.append("..")

from selenium_scraper.twitter_scraper import Twitter_Scraper

# Path to save the scraped tweets
# OUTPATH = "../data/raw/tweets"

# Inputs needed
# EMAIL = input("Enter your email: ")
# USERNAME = input("Enter your username: ")
# PASSWORD = input("Enter your password: ")

EMAIL = "email"
USERNAME = "username"
PASSWORD = "password"

scraper = Twitter_Scraper(
    mail=EMAIL,
    username=USERNAME,
    password=PASSWORD,
)

print("Logging in...")

# Login to Twitter
# scraper.login()

print("Starting to scrape tweets...")

# Scrape tweets from 2014-2015
# scraper.scrape_tweets(
#     max_tweets=100,
#     scrape_query='"field museum" since:2022-04-01 until:2022-04-02',
# )

scraper.save_to_csv(file_path='tweet_test.csv')

