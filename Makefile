# In a Makefile, .PHONY is a special target that tells make that the targets listed as
# dependencies of .PHONY are not actual files. Instead, they are just labels for commands 
# to be executed. This is useful to avoid conflicts with files that might have the same 
# name as the targets.

.PHONY: clean create_environment requirements

## GLOBALS

PROJECT_NAME = "museum-twitter"
PYTHON_INTERPRETER = python

## UTILITIES

clean:
	rm -f **/*/.DS_store

create_environment:
	$(PYTHON_INTERPRETER) -m venv env

requirements:
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

# then I can run `make requirements` in shell to install the requirements!

## SCRAPING TWEETS

# Get tweet data from Bristol Museum
tweets: data/interim/bristol_tweets_2015_2019.csv
	$(PYTHON_INTERPRETER) src/scrape_tweets.py

## EXTERNAL DATASETS

# Download climate data
climate: data/raw/meteostat_lyneham.csv
	$(PYTHON_INTERPRETER) src/data/get_climate.py

# Download visitor data
visitors: data/raw/bristol_visitors.csv
	curl -o data/raw/bristol_visitors.csv 'https://hub.arcgis.com/api/v3/datasets/98d95d36536343eca59e6e4bb04c58b7_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1'


## PLOTS

plots:
	$(PYTHON_INTERPRETER) src/plotting.py
