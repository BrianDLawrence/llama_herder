from config import GENERAL
from ai_agent import LlamaAgent
from .test_data import TESTPROMPT

def test_llama_brain_can_be_initialized():
    ollama = LlamaAgent(GENERAL,TESTPROMPT)
    assert isinstance(ollama,LlamaAgent)
