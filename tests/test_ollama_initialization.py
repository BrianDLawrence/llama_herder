import pytest
import ai_agent 
from langchain_community.llms import Ollama


def test_llama2_initialization():
    llm2 = ai_agent.initialize_llama2()
    # llm2("Tell me a short joke about star trek")
    assert isinstance(llm2,Ollama)


def test_wizardmath_initialization():
    mathwiz = ai_agent.initialize_mathwiz()
    # mathwiz("How many 4-digit numbers have the last digit equal to the sum of the first two digits?")
    assert isinstance(mathwiz,Ollama)