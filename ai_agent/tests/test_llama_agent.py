from unittest.mock import MagicMock
from unittest.mock import patch
import pytest
from ai_agent.llama_agent import LlamaAgent
# pylint: disable=redefined-outer-name

MODEL = 'test_model'
PROMPT = 'test_prompt'

@pytest.fixture
def mock_llm_chain(mocker):
    mock_chain_class = mocker.patch('ai_agent.llama_agent.LLMChain')
    mock_chain_instance = MagicMock()
    mock_chain_class.return_value = mock_chain_instance
    return mock_chain_class, mock_chain_instance

@patch('ai_agent.llama_agent.initialize_ollama')
def test_initialize_the_agent(mock_initialize_ollama, mock_llm_chain):

    LlamaAgent(MODEL, 'test_prompt')

    mock_initialize_ollama.assert_called_once_with(MODEL)
    mock_chain_class = mock_llm_chain[0]
    mock_chain_class.assert_called_once_with(llm=mock_initialize_ollama.return_value, prompt=PROMPT, verbose=False)

def test_request_with_mocked_dependencies(mock_llm_chain):

    user_input = 'hello'
    expected_response = 'hello world'
    mock_llm_chain_instance = mock_llm_chain[1]
    mock_llm_chain_instance.invoke.return_value = {"text": expected_response}

    agent = LlamaAgent(MODEL, PROMPT)
    response = agent.request(user_input)

    assert response == expected_response
    mock_llm_chain_instance.invoke.assert_called_once_with(f"{user_input}")
    assert agent.history == [user_input, expected_response], "Expected both input and response to be in history"

def test_request_handles_exception(mock_llm_chain):

    exception_message = 'Test exception'
    mock_llm_chain_instance = mock_llm_chain[1]
    mock_llm_chain_instance.invoke.side_effect = Exception(exception_message)

    agent = LlamaAgent(MODEL, PROMPT)

    with pytest.raises(Exception) as exc_info:
        agent.request('hello')

    assert str(exc_info.value) == exception_message