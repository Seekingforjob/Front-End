import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://hilhtjts:H48lD7TxF_1DQdcZhBOsOvFpmgJOmwQW@otter.rmq.cloudamqp.com/hilhtjts"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news"

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://qaxmxozt:k7_R-cmOcZbdORt5LUWktg2F1vTsRS9u@otter.rmq.cloudamqp.com/qaxmxozt"
DEDUPE_NEWS_TASK_QUEUE_NAME = "dedupe-news"

def clearQueue(queue_url, queue_name):
    scrape_news_queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.getMessage()
            if msg is None:
                print("Cleared %d messages." % num_of_messages)
                return
            num_of_messages += 1


if __name__ == "__main__":
    clearQueue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
    clearQueue(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)