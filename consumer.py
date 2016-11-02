from kafka import KafkaConsumer

KAFKA_HOST = 'localhost:9092'
TOPIC = 'twitter_feeds'
TIMEOUT = 10000

def main():
    
    # KafkaConsumer Object
    consumer = KafkaConsumer(TOPIC, bootstrap_servers=[KAFKA_HOST],
                             consumer_timeout_ms=-1)

    # read messages and get tweet text
    for message in consumer:
        print "Received tweet:", message.value, "\n"

if __name__ == '__main__':
    main()
