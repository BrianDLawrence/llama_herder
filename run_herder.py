"""
Main python program to run the herder
This is a work in progress and not CLEAN at all
But it will be :) 
"""
import multiprocessing
from message_handler import Handler
from rag_handler import Handler as RagHandler
from ai_agent import Agent
from longterm_memory import LlamaMemory
from config import CLOUDAMQP_URL, GENERAL

def start_listeners():
    simple_action_listener = multiprocessing.Process(target=start_simple)
    simple_action_listener.start()

def start_simple():
    handler = Handler(CLOUDAMQP_URL)
    print("Starting simple action listener on channel hub ")
    handler.listen("hub",callback)

# pylint: disable=unused-argument
def callback(ch, method, properties, body):
    """ 
    callback function which will be called by pika
    Note the pylint disable because we don't need 
    all these params at the moment.
    """
    print('Received in hub')
    print(body)

    rag_hanlder = RagHandler("http://localhost:5174",10)

    urls = rag_hanlder.parse_urls(body.decode("utf-8"))
    if len(urls) > 0:
        print("Calling with the following URL(s)")
        print(urls)
        rag_data = rag_hanlder.process_urls(urls)
        print(rag_data)
        call_agent_with_memory(body,str(rag_data))
    else:
        agent = Agent(GENERAL)
        response = agent.make_request(body.decode("utf-8"))
        print(response)

def call_agent_with_memory(body:str,string_to_remember:str):
    memory = LlamaMemory()
    memory.remember_string(string_to_remember)
    agent = Agent(GENERAL,memory)
    response = agent.make_request(body.decode("utf-8"))
    print(response)

if __name__ == "__main__":
    start_listeners()
