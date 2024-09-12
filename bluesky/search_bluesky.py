# function to search bluesky for posts containing a specific query

from datetime import datetime
import requests
import json
import pandas as pd
import re


def search_bluesky(query, since_date, until_date, lim=100):

    # Check if the query is more than one word
    if len(query.split()) > 1:
        query = f'"{query}"'

    # Add the time to the date to get the API to work properly
    time_string = 'T00:00:00Z'

    # Some things that are needed for the API call below
    payload = {}
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer <TOKEN>'}
    url = f"https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts?q={query}&limit={lim}&since={since_date}{time_string}&until={until_date}{time_string}"

    # make the request
    response = requests.request("GET", url, headers=headers, data=payload)

    # Parse the JSON response
    data = json.loads(response.text)

    # Extract and return relevant information in a DataFrame
    posts_data = []
    for post in data.get('posts', []):
        post_info = {
            'User': post['author']['handle'],
            'Content': post['record']['text'],
            'Timestamp': post['record']['createdAt'],
            'Likes': post['likeCount'],
            'Reposts': post['repostCount']
        }
        posts_data.append(post_info)
    
    # Print the number of posts
    num_posts = len(data.get('posts', []))
    print(f"Number of posts: {num_posts}")

    # Create a DataFrame
    df = pd.DataFrame(posts_data)

    # Replace 'T' and 'Z' and convert to datetime format YYYY-MM-DD
    df['Timestamp'] = df['Timestamp'].str.replace('T', ' ').str.replace('Z', '')
    
    # Strip nonimportant info
    times = df['Timestamp']
    times = [re.findall(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}', x) for x in times]
    df['date'] = times
    # Convert to datetime
    df['date'] = pd.to_datetime(df['date'].str[0], format='%Y-%m-%d %H:%M')
    # Remove the original timestamp column
    df = df.drop(columns=['Timestamp'])

    # Return the DataFrame
    return df

# test
# df = search_bluesky(query="'Field Museum'", since_date="2024-09-01", until_date="2024-09-30")
# df.head()

def date_range(start, end, intv):
    from datetime import datetime
    start = datetime.strptime(start,"%Y-%m-%d")
    end = datetime.strptime(end,"%Y-%m-%d")
    diff = (end  - start ) / intv
    for i in range(intv):
        yield (start + diff * i).strftime("%Y-%m-%d")
    yield end.strftime("%Y-%m-%d")

def search_bluesky_batch(query, since_date, until_date, lim=100, nbatch=1, timefmt=False):
    # Get the date range
    date_range_list = list(date_range(start=since_date, end=until_date, intv=nbatch))
    # Create an empty DataFrame
    df = pd.DataFrame()
    # Loop over the date ranges
    for i in range(len(date_range_list)-1):
        df_batch = search_bluesky(query=query, since_date=date_range_list[i], until_date=date_range_list[i+1], lim=lim)
        df = pd.concat([df, df_batch])
    return df

# testing
# tmp = search_bluesky_batch(query="'Field Museum'", since_date="2023-05-01", until_date="2024-09-11", nbatch=20)
# works!

# search_bluesky(query="'Field Museum'", since_date="2023-01-01", until_date="2023-01-31")

# date_range_list = list(date_range(start=since_date, end=until_date, intv=nbatch))
