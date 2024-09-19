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

print(EMAIL, USERNAME, PASSWORD)

