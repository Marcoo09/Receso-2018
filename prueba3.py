#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import tweepy
import wget

#Get your Twitter API credentials and enter them here
consumer_key = "OUMVClAUcCigm4nBrpjODh5CY"
consumer_secret = "2ZwQ2RXr0QE0w0GGepm6vKHGeg9k6JHYYDRBKQfYtmssC7dQOs"
access_key = "1402351832-8m7eedL0PADtnnPGY4B0SbpKI7A68Tb7bApP9Bq"
access_secret = "CdsQKvUxFugmds1nxwgQ7YxvztHkBbFPIQXfo1MlCQp0C"

@classmethod
def parse(cls, api, raw):
    st = cls.first_parse(api, raw)
    setattr(st, 'json', json.dumps(raw))
    return st

def init_tweepy():
  # Status() is the data model for a tweet
  tweepy.models.Status.first_parse = tweepy.models.Status.parse
  tweepy.models.Status.parse = parse
  # User() is the data model for a user profil
  tweepy.models.User.first_parse = tweepy.models.User.parse
  tweepy.models.User.parse = parse

#method to get a user's last 100 tweets
def get_tweets(username):
  #http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api = tweepy.API(auth)

  #set count to however many tweets you want; twitter only allows 100 at once
  number_of_tweets = 100

  #get tweets
  tweets = api.user_timeline(screen_name = username,count = number_of_tweets)

  #create array of tweet information: username, tweet id, date/time, text
  tweets_for_csv = [[username,tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

  #write to a new csv file from the array of tweets
  print ("writing to {0}_tweets.csv".format(username))
  with open("{0}_tweets.csv".format(username) , 'w+') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(tweets_for_csv)

  tweets = api.user_timeline(screen_name=username,
                           count=10000, include_rts=False,
                           exclude_replies=True)
  last_id = tweets[-1].id

  media_files = set()
  for status in tweets:
      print(status)
      media = status.entities.get('media', [])
      if(len(media) > 0):
          media_files.add(media[0]['media_url'])

  for media_file in media_files:
    wget.download(media_file,out="./pictures")
    print("Estoy descargando")

#if we're running this as a script
if __name__ == '__main__':
    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print ("Error: enter one username")