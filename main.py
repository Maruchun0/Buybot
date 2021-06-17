import time
import twitter

def retrieveTweets():
    last_tweet_retrieved = 0
    while True:
        X = twitter.main(last_tweet_retrieved)
        last_tweet_retrieved = int(X[1])
        print(X[0])
        time.sleep(300)

retrieveTweets()
