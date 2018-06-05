#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tweepy
import csv
import re

def getTweets(userName):
  def retrieveText(texts):
    pattern_http = r"http"
    pattern_www = r"www"

    for i, line in enumerate(texts):
      matchOB1 = re.match(pattern_http , line)
      matchOB2 = re.match(pattern_www , line)
      if matchOB1 or matchOB2:
          texts.pop(i)
      return texts

  consumer_key = 'U18eEXpUj0AGNEi1OzgyEhnXy'
  consumer_secret = 'd0eylF4oaNoYhDT9R03T1YWepKVIM0OXTjPZBkMtj0YcJOMZw1'
  access_key = '957995440649179136-pj1MbYT1DAqAlPQkxJj6i7rrkE6C4cp'
  access_secret = 'TuyjwmHvXKbA6gv15LqcgQuzxVQbGV0DMecL2qC2CXZxv'

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api = tweepy.API(auth)

  #ツイート取得
  tweet_data = []

  for tweet in tweepy.Cursor(api.user_timeline,screen_name = userName,exclude_replies = True).items():
      tweet_data.append(tweet.text.replace('\n','').replace('http','').replace('www',''))
  print(tweet_data)
  for i, line in enumerate(tweet_data):
    if len(line) == 0:
      tweet_data.pop(i)
  #tweet_data = retrieveText(tweet_data)
  #csv出力
  with open('tweets_20170805.csv', 'w',encoding='utf-8') as f:
      writer = csv.writer(f)
      writer.writerow(["text"])
      writer.writerows(tweet_data)
  pass

  return tweet_data

if __name__ == '__main__':
  userName = "dwoods89"
  getTweets(userName)