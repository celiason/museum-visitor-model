# Sentiment analysis and museums

## Intro

This project looks at visitor data and social media timelines to predict lags/changes in visitor rates.

## Data sets

- Museum visitor data obtained from the Bristol Museum [](https://opendata.bristol.gov.uk)
- Tweets containing "Bristol Museum" (see data/processed folder)

## Results

I used random forest regression models implemented in the `sklearn` python module.

The best model had an accuracy ($R^2$) of 87%, which is pretty good. You can see in the figure below that the model (red dashed line) is doing a pretty good job at predicting changes in the actual number of daily visitors over time (blue line).

![Predicted Visitors](figs/visitors_predicted.png)
**Figure 1:** Actual and predicted number of visitors to the Bristol Museum from 2015-2019.

Using `TextBlob` in python, I also ran a model that predicted sentiment from the content of tweets from 2015-2019 (see code for scraping from X). You can see these data plotted below. There is a really big spike at the beginning of 2018 that corresponds to some negative press the Bristol Museum had from a Banksy piece being displayed.

![Twitter sentiment](figs/timeline_sentiment_bristol.png)

## Insights

Using the random forest model, I found that the top 3 most important features that predict visitor numbers are weekend (0.20 importance), max. temperature (0.11), and whether there is a new exhibit on display (0.11).

The most important feature that predicts visitor numbers is WEEKEND, with about 700 more visitors per day. This makes sense given that kids are out of school, adults are not working, and people are just more interested in doing things on the weekend.

Maximum temperature showed an overall negative effect on visitors, but this effect was conditional on the time of week, among other factors. For example, on weekends max. temperature doesn't really have any effect on visitor rates, but on weekdays there is a more pronounced effect with about 200 fewer visitors per day.

EXHIBITS had a large effect too, with around 400 more visitors on a given day.

## Author

Chad M. Eliason  
Field Museum
