import tweepy as tw
import json
import settings
import requests
import os

os.chdir("D:\Computer\Documents\GitHub\Buybot")

def create_headers(bearer_token):   #Creates headers for requests
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(query_field):    #Creates a API URL for requests
    url = f'https://api.twitter.com/2/tweets/search/recent?query={query_field}'
    return url

def connect_to_endpoint(url, headers):  #Connects to API URL endpoint
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def sortTweets(data, last_tweet_retrieved):
    Tweets = []
    for i in range(len(data)):
        if int(data[i]['id'])>last_tweet_retrieved:
            Tweets.append(data[i]['text'])
        else : return Tweets
    return Tweets

def main(last_tweet_retrieved):
    headers = create_headers(settings.bearer_token)
    url = create_url('from:SupyJP')
    data = connect_to_endpoint(url, headers)
    jsonString = json.dumps(data, indent = 4, sort_keys = True)
    jsonFile = open("request.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    with open('request.json') as f:
        file = json.load(f)
    goodTweets = sortTweets(file['data'], last_tweet_retrieved)
    print("Request Done")
    return (goodTweets, file['meta']['newest_id'])
