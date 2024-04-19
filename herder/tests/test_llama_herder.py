import unittest
from unittest.mock import patch, MagicMock, call
from herder import LlamaHerder

class TestLlamaHerder(unittest.TestCase):

    def setUp(self) -> None:
        self.user = MagicMock()
        self.helper = MagicMock()
        return super().setUp()

    @patch('herder.llama_herder.Agent')
    def test_initialize_the_herder(self, mock_agent):
        model = "test model"
        LlamaHerder(model, model)
        calls = [call(model), call(model)]
        mock_agent.assert_has_calls(calls)

    def test_herd_goal_achieved(self):

        self.user.make_request_with_template.return_value = "THE GOAL IS COMPLETE! Your Chat History is: {}"
        self.helper.make_request_with_template.return_value = "Some response"
        lh = self.create_test_herder()

        result = lh.herd("Goal", "Context")
        self.assertIn("THE GOAL IS COMPLETE!", result)

    def test_herd_helper_cannot_help(self):

        self.user.make_request_with_template.return_value = "Some user response"
        self.helper.make_request_with_template.return_value = "I CAN'T HELP Your Chat History is: {} The request is: {}"

        lh = self.create_test_herder()

        result = lh.herd("Goal", "Context")
        self.assertIn("GOAL NOT ACHIEVED", result)

    def test_herd_max_conversations(self):

        self.user.make_request_with_template.side_effect = ["User response 1", "User response 2", "User response 3"]
        self.helper.make_request_with_template.side_effect = ["Helper response 1",
                                                              "Helper response 2", "Helper response 3"]

        lh = self.create_test_herder()

        result = lh.herd("Goal", "Context")
        self.assertEqual(self.user.make_request_with_template.call_count, 3)
        self.assertEqual(self.helper.make_request_with_template.call_count, 3)
        self.assertIn("GOAL NOT ACHIEVED MAXATTEMPS", result)

    def create_test_herder(self):
        lh = LlamaHerder("test model", "test model")
        lh.user = self.user
        lh.helper = self.helper
        return lh
