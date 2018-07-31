import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'OUMVClAUcCigm4nBrpjODh5CY'
consumer_secret = '2ZwQ2RXr0QE0w0GGepm6vKHGeg9k6JHYYDRBKQfYtmssC7dQOs'
access_token = '1402351832-8m7eedL0PADtnnPGY4B0SbpKI7A68Tb7bApP9Bq'
access_token_secret = 'CdsQKvUxFugmds1nxwgQ7YxvztHkBbFPIQXfo1MlCQp0C'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('wwplus.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#workwithplus",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])