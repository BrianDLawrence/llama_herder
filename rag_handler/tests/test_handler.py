from unittest.mock import patch, Mock
import unittest
from rag_handler import Handler

class TestHandler(unittest.TestCase):
    def setUp(self):
        self.test_rag_service_url = "testurl"
        self.handler = Handler(self.test_rag_service_url,10)

    def test_initialize_the_handler(self):
        handler = Handler(self.test_rag_service_url,10)
        self.assertIsInstance(handler, Handler)
        self.assertEqual(handler.rag_service_url, self.test_rag_service_url)

    @patch('rag_handler.handler.requests.post')
    def test_invoke_service_with_one_url(self, mock_post):

        test_url = "http://example.com"
        expected_response = {
            "url": test_url,
            "content": "test website content"
        }
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = [expected_response]

        result = self.handler.process_urls([test_url])

        mock_post.assert_called_once_with(f"{self.test_rag_service_url}/process-urls", json=[test_url],timeout=10)
        self.assertEqual(result, [expected_response])

    def test_parse_urls_single_url(self):
        test_input = "This is a test input for a url https://test.com OK?"
        expected_output = ["https://test.com"]

        self.assertEqual(self.handler.parse_urls(test_input),expected_output)

    def test_parse_urls_two_url(self):
        test_input = "This is a test input for a url https://test.com OK, and https://test2.com"
        expected_output = ["https://test.com","https://test2.com"]

        self.assertEqual(self.handler.parse_urls(test_input),expected_output)

    def test_parse_urls_no_url(self):
        test_input = "This is a test input for no urls"
        expected_output = []

        self.assertEqual(self.handler.parse_urls(test_input),expected_output)
