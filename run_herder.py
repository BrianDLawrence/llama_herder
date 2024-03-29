"""
Main python program to run the herder
This is a work in progress and not CLEAN at all
But it will be :) 
"""
import pika
from ai_agent import Agent
from config import CLOUDAMQP_URL, GENERAL

params = pika.URLParameters(CLOUDAMQP_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='hub')

# pylint: disable=unused-argument
def callback(ch, method, properties, body):
    """ 
    callback function which will be called by pika
    Note the pylint disable because we don't need 
    all these params at the moment.
    """
    print('Received in hub')
    print(body)
    singleagent = Agent(GENERAL)
    response = singleagent.make_request(body.decode("utf-8"))
    print(response)


if __name__ == "__main__":
    channel.basic_consume(queue='hub', on_message_callback=callback, auto_ack=True)

    print('Started Consuming')

    channel.start_consuming()

    channel.close()
