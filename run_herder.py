import pika
from ai_agent import LlamaAgent
from config import CLOUDAMQP_URL, GENERAL, GENERALPROMPT

params = pika.URLParameters(CLOUDAMQP_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='hub')

def callback(ch, method, properties, body):
    print('Received in hub')
    print(body)
    singleagent = LlamaAgent(GENERAL,GENERALPROMPT)
    response = singleagent.request(body.decode("utf-8"))
    print(response)
   
channel.basic_consume(queue='hub', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()