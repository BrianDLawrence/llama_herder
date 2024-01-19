import pytest
import ai_agent 
from ai_agent import LlamaBrain
from langchain_community.llms import Ollama

def test_LLama_Brain():
    brain = LlamaBrain()
    assert isinstance(brain,LlamaBrain)
    response = brain.think("I am testing that you are working - if you are working, please respond with a single YES")
    assert response == "YES"