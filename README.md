# Sentiment analysis and museums

## Data sets

- Museum visitor data obtained from the Bristol Museum [](https://opendata.bristol.gov.uk)
- Tweets containing "Bristol Museum" (see data/processed folder)
- Weather data downloaded using `meteostat`

## Overview

This project looks at visitor data and social media timelines to predict lags/changes in visitor rates. Below is a plot showing changes in the number of visitors over time. The drops to zero that become more common in 2018-2019 are cases where the museum is closed (more on that below). On average, there were 1125 visitors per day from Apr 2015 - Feb 2019, the extent of the dataset. Among full years, the greatest number of visitors came to the museum in 2018 (416k) and the fewest came in 2016 (346k). 

![](figs/visitors_bristol.png)

## Twitter results

The new X twitter API is prohibitively expensive, therefore I used [Selenium](https://github.com/godkingjay/selenium-twitter-scraper) to scrape tweets from twitter between 2015 and 2019 (see `scraping_brisol.py` and `scraper/` for code used). In total, I obtained __6281__ tweets from 2015 - 2019. Of those, __3133__ were put out by the museum and __3148__ were tweeted by other twitter handles.

To understand the importance of public perception on museum visitor rates, I calculated three metrics:

1. Promotion - the number of museum tweets
2. Engagement - the number of user tweets, retweets, and likes
3. Sentiment - the average sentiment value of user tweets

To calculate sentiment, I used the `TextBlob` in python to predict sentiment from the content of user tweets between 2015-2019. Below is a wordcloud (generated with the `wordcloud` module in python).

![](figs/wordcloud.png)

I averaged twitter sentiments by day and then plotted over time. You can see these data plotted below. There is a really big spike at the beginning of 2018 that corresponds to some negative press the Bristol Museum had over an apparent dispute of the display of a Banksy piece (see news article [here](https://www.bbc.com/news/uk-england-bristol-42708000)).

![Twitter sentiment](figs/timeline_sentiment_bristol.png)

## Challenges with the data

I filtered out website links and common words not useful in calculating sentiment. In many cases, tweets with negative sentiment had the word "death" in them. Most of these tweets were actually positive and related to the Death exhibit in 2015. To fix this, I added "death" to the list of stop words prior to sentiment analysis with `TextBlob`. 

Some of the days hade missing weather data. I got around this challenge by using data imputation methods implemented in the `sklearn` module (see Jupyter notebook for details).

Several drops in visitor numbers were due to the musem being closed. This allowed me to create a categorical variable (closed or open) by determining whether visitor numbers were zero for a given day.

One potential problem with predicting future visitor numbers is that my model might only be relevant for a given year (or set of years). To rule this out, I fit a random forest regression model with year as a predictor and found that this variable was insignificant (all importance values < 0.03) in explaining variation in visitor numbers among years. This increased my confidence that the model is relevant for current (and future) visitor numbers at the Bristol Museum.

## Modeling visitor rates

I used random forest regression models implemented in the `sklearn` python module. The best model had an $R^2$ scores of 0.869. This means that the model can predict the number of visitors with about 87% accuracy, which is pretty darn good. You can see in the plot below that the model (red dashed line) is doing a pretty good job at tracking the actual number of daily visitors over time (blue line).

![Predicted Visitors](figs/visitors_predicted.png)

Using the random forest regression model, I found that the top 3 most important features that predict visitor numbers are weekends (importance score = 0.198), maximum temperature (importance score = 0.110), and whether there was a new exhibit on display (importance score = 0.107).

The most important feature that predicts visitor numbers is weekends, with about 700 more visitors attending the museum per weekend day. This makes sense given that kids are out of school, adults are not working, and people are probably just more interested in doing things on the weekend.

The display of special exhibits also had a large effect, attracing around 400 more visitors per day.

![](figs/pdp_weekend.png)

Maximum daily temperature (TMAX) showed an overall negative effect on visitors, but this effect was conditional on the time of week, among other factors. For example, on weekends, TMAX doesn't really have any effect on visitor rates, but on weekdays there is a more pronounced effect with about 200 fewer visitors per day.

<!-- ![](figs/pdp_weekend_tmax.png) -->

The large jump in Jul 2015 (see plot above) corresponds to the opening of the Art Forms in Nature exhibit. Compared to other exhibition openings, this one was more profitable, possibly because it opened in the summer when TMAX was high and school as off.

## Rain, rain, go away

It is interesting to look at the ineracting effects between precipitation (0.066) and windspeed (0.070 importance scores). The partial dependence plot shown below suggest that about 142 more people come to the museum on calm, rainy days than on windy, dry days.

![](figs/pdp_wspd_prcp.png)

## What makes a good day at the museum?

Another way to look at the data is with waterfall charts. These are commonly used in the financial sector.

Below is a waterfall chart for the day with the greatest number of visitors (August 22, 2015). The features are ordered by their effect on the baseline (0). We see that TMAX has the greatest effect (resulting in 1154 more visitors compared to the average). This makes sense if people are out and want to get out of the heat and into an air-conditioned space (the maximum tempeterature that day was 27.8 C or 82 F). It's also interesting to see that there was net positive sentiment on twitter that day that also contributed to ~66 more visitors.

The ongoing special exhibit "Death: The Human Experience" attracted another 536 visitors, and the fact that this day was a weekend brought in 528 more than average. The net effect of all the predictors was 2840 more visitors than baseline of 1127 visitors.

![](figs/waterfall_max.png)

## Insights

- To capitalize on potential revenue from high visitor volumes, it would make sense to plan exhibition openings and special events, discount food days etc. when summer peak temperatures are expected to be high (TMAX >28 C).

- Although it is of course not surprising that museum closing was a strong predictor of visitor numbers in the model, to maximize visitor volume, it would make sense to close the museum more frequently in the spring then TMIN is low (TMIN had a 0.08 importance rating) and overall visitor numbers are decreased with kids back in school.

- The number of tweets put out by the Bristol Museum had little effect on visitors (0.03 importance score), and there was a flatline after 5-10 tweets per day, suggesting that this would be an optimal number going forward to optimize time budgets (of social media staff, etc).

## Future directions

I can test this model with visitor data from other large museums

Incorporate more features into the model

Optimize the sentiment analysis as it was missing many cases (e.g., the Death exhibit often yielded negative sentiments although the exhibit received high praise and resulted in a jump in visitor rates).

Forecast overall revenue by calculating the area under the curve based on weather predictions and historic date. Assuming a visitor purchases on average $20 USD in food and $12 USD in special exhibit tickets, and accounting for historical and future fluctuations in climate, I could predict total revenues for 2025 based on my model.

<!-- maybe 1/10 people buy a ticket?? -->

## Author

Chad M. Eliason  
Field Museum
