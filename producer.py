from twython import Twython
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError

TWITTER_APP_KEY = 'l5NP1KQZxSvlAqNOd5pfKpe8r' #supply the appropriate value
TWITTER_APP_KEY_SECRET = 'pBepdXoxDjREgqjeSQYltBqJ9PGKoXUtMgOXJOOZwdO88AAvTF'
TWITTER_ACCESS_TOKEN = '2407434150-29RUn5YRhBQOZgSUEy5HnjjTdPIIlSYgzZHGduL'
TWITTER_ACCESS_TOKEN_SECRET = '4hUMANOqyxVjfw0i0uAIbEOYsqs25IDD7bHPE3AP5QKEw'

KAFKA_HOST = 'localhost:9092'
TOPIC = 'twitter_feeds'

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

def get_tweets(keyword):

    search = t.search(q=keyword,count=100)   #**supply whatever query you want here**
    tweets = []

    tweets = search['statuses']

    #print len(tweets)
    for tweet in tweets:
            print "Sending tweet:", str(tweet['text']), "\n"
            producer.send(TOPIC,str(tweet['text']))
            time.sleep(1)


def twittmap():
    try:
        get_tweets('trump')
        """get_tweets('clinton')
        get_tweets('worlds')
        get_tweets('music')
        get_tweets('food')
        get_tweets('java')
        get_tweets('scala')
        get_tweets('flask')
        get_tweets('movie') """
    except:
        print "OOPs! You have reached rate limit !!"
        time.sleep(5)
        return

def main():

    while True:
        twittmap()


if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=[KAFKA_HOST])
    main()


