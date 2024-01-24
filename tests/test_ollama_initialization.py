""" Testing ollama brain """
from ai_agent import LlamaBrain

def test_llama_brain_initialization():
    """ Testing initialization of the brain """
    brain = LlamaBrain()
    assert isinstance(brain,LlamaBrain)