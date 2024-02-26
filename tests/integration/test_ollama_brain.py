""" Testing ollama agent can be invoked 
    For this test to run, it requires
    a local Ollama LLM service 
"""
from config import GENERAL
from ai_agent import LlamaAgent
from .test_data import TESTPROMPT

def test_llama_is_able_to_be_invoked():
    ollama = LlamaAgent(GENERAL,TESTPROMPT)
    prompt = """This is a pytest, I am checking to see if you are running.
    If you are running, please respond with a single 'I AM WORKING' and nothing else"""
    response = ollama.request(prompt)
    assert "I AM WORKING" in response

def test_llama_remembers_our_chats():
    dogsname = "Chuck"
    ollama = LlamaAgent(GENERAL,TESTPROMPT)
    prompt = """This is a pytest, I am checking to see if you are running and working correctly.
      I want you to remember this: The dog's name is """+dogsname
    ollama.request(prompt)
    prompt2 = "Please tell me the dog's name."
    response = ollama.request(prompt2)
    assert dogsname in response
