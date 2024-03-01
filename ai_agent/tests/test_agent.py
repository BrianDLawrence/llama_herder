from unittest.mock import patch
from ai_agent import Agent
from ..utils.llm_constants import DEFAULT_TEMPLATE

MODEL = 'test_model'
PROMPT = "test prompt"

@patch('ai_agent.agent.ChatOllama')
def test_initialize_the_agent(mock_chatollama):
    Agent(MODEL)
    mock_chatollama.assert_called_once_with(model=MODEL)

@patch('ai_agent.agent.ChatPromptTemplate.from_template')
@patch('ai_agent.agent.StrOutputParser')
def test_invoke_llm_simple(mock_stroutputparser,mock_from_template):
    agent = Agent(MODEL)
    agent.make_request(PROMPT)
    mock_from_template.assert_called_once_with(DEFAULT_TEMPLATE)
    mock_stroutputparser.assert_called_once()

@patch('ai_agent.agent.ChatPromptTemplate.from_template')
@patch('ai_agent.agent.StrOutputParser')
def test_invoke_llm_with_template(mock_stroutputparser,mock_from_template):
    template = "test template"
    agent = Agent(MODEL)
    agent.make_request_with_template(PROMPT,template)
    mock_from_template.assert_called_once_with(template)
    mock_stroutputparser.assert_called_once()

@patch('ai_agent.agent.ChatOllama.invoke')
def test_the_history(mock_invoke):
    mock_invoke.return_value = "hello"
    agent = Agent(MODEL)
    assert agent.get_history_as_string() == ""
    assert agent.make_request(PROMPT) == "hello"
    assert agent.get_history_as_string() == "hello"
    mock_invoke.return_value = "how are you"
    assert agent.make_request(PROMPT) == "how are you"
    assert agent.get_history_as_string() == "hello how are you"
