from unittest.mock import patch,call
from herder import LlamaHerder

@patch('herder.llama_herder.Agent')
def test_initialize_the_herder(mock_agent):

    model = "test model"
    LlamaHerder(model,model)
    calls = [call(model), call(model)]
    mock_agent.assert_has_calls(calls)
