from unittest.mock import patch, Mock
import unittest
from message_handler import Handler

class TestHandler(unittest.TestCase):
    def setUp(self):
        self.mock_urlparameters = patch('message_handler.handler.pika.URLParameters').start()
        self.mock_blockingconnection = patch('message_handler.handler.pika.BlockingConnection').start()
        self.mock_connection = self.mock_blockingconnection.return_value
        self.mock_channel = Mock()
        self.mock_connection.channel.return_value = self.mock_channel
        self.addCleanup(patch.stopall)

    def test_initialize_the_handler(self):

        test_amqp_url = "testurl"
        handler = Handler(test_amqp_url)
        assert isinstance(handler,Handler)
        assert handler.cloud_amqp_url == test_amqp_url

    def test_queue_declare_called(self):
        test_amqp_url = "testurl"
        handler = Handler(test_amqp_url)
        test_queue = "testqueue"
        handler.listen(test_queue, lambda x, y, z: None)
        self.mock_channel.queue_declare.assert_called_once_with(queue=test_queue)

    def test_basic_consume_setup(self):
        test_amqp_url = "testurl"
        handler = Handler(test_amqp_url)
        test_queue = "testqueue"
        # pylint: disable=unnecessary-lambda-assignment
        test_callback = lambda x, y, z: None
        handler.listen(test_queue, test_callback)
        self.mock_channel.basic_consume.assert_called_once_with(queue=test_queue,
        on_message_callback=test_callback, auto_ack=True)

    def test_start_consuming_and_close_called(self):
        test_amqp_url = "testurl"
        handler = Handler(test_amqp_url)
        test_queue = "testqueue"
        handler.listen(test_queue, lambda x, y, z: None)
        self.mock_channel.start_consuming.assert_called_once()
        self.mock_channel.close.assert_called_once()
