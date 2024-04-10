"""
Main python program to run the herder
This is a work in progress and not CLEAN at all
But it will be :) 
"""
from message_handler import Handler
from ai_agent import Agent
from config import CLOUDAMQP_URL, GENERAL

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
    handler = Handler(CLOUDAMQP_URL)
    handler.listen("hub",callback)
