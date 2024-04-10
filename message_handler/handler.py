import pika

class Handler:

    def __init__(self,cloud_amqp_url):
        self.cloud_amqp_url = cloud_amqp_url

    def listen(self,queue,callback):
        channel = self.create_channel()
        self.prepare_channel(channel,queue,callback)
        self.start_listening(channel)

    def create_channel(self):
        params = pika.URLParameters(self.cloud_amqp_url)
        connection = pika.BlockingConnection(params)
        return connection.channel()

    def prepare_channel(self,channel,queue,callback):
        channel.queue_declare(queue=queue)
        channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    def start_listening(self,channel):
        channel.start_consuming()
        channel.close()
