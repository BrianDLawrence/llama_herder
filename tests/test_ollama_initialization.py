""" Testing ollama brain """
from config import GENERAL
from ai_agent import LlamaAgent
from .test_data import TESTPROMPT

def test_llama_brain_initialization():
    """ Testing initialization is working """
    ollama = LlamaAgent(GENERAL,TESTPROMPT)
    assert isinstance(ollama,LlamaAgent)
