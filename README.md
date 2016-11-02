# Kafka-Twitter
Using Kafka and Zookeeper to stream Twitter data

This is a demo project for a single node Kafka cluster for streaming tweets in real time from twitter and storing it.
We demonstrate the same as a Kafka Producer and Consumer Problem.

Requirements

Apache Kafka Framework
Python modules mentioned in requirements.txt
Install Dependencies

pip install -r requirements.txt
Download and unzip/untar the Apache Kafka Framwork
Run the twitter-kafka demo

cd to kafka framework folder
Start zookeeper server: bin/zookeeper-server-start.sh config/zookeeper.properties
Start kafka sever: bin/kafka-server-start.sh config/server.properties

Add your twitter keys to the producer.py file 
Get tweets and add to Kafka Topic in one terminal: python producer.py
Consume from the Topic: python consumer.py
