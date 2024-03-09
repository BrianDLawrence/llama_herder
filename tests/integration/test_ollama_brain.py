""" Testing ollama agent can be invoked 
    For this test to run, it requires
    a local Ollama LLM service 
"""
from config import GENERAL
from ai_agent import Agent
from longterm_memory import LlamaMemory

def test_agent_is_working():
    agent = Agent(GENERAL)
    prompt = """This is a pytest, I am checking to see if you are running.
    If you are running, please respond with a single 'I AM WORKING' and nothing else"""
    response = agent.make_request(prompt)
    print(response)
    assert "I AM WORKING" in response

def test_agent_remembers_our_chats():
    dogsname = "Chuck"
    ollama = Agent(GENERAL)
    prompt = """This is a pytest, I am checking to see if you are running and working correctly.
      I want you to remember this: The dog's name is """+dogsname
    ollama.make_request(prompt)
    prompt2 = "Please tell me the dog's name."
    response = ollama.make_request(prompt2)
    assert dogsname in response

def test_agent_is_working_with_memory():
    string_to_remember = "Brian's cat is named Arturo"
    memory = LlamaMemory()
    memory.remember_string(string_to_remember)
    agent = Agent(GENERAL,memory)
    prompt = """This is a pytest, I am checking to see if you are running and have memory.
    The chat history will be empty. You should find context however.
    Please tell me what Brian's cat's name is"""
    response = agent.make_request(prompt)
    print(response)
    assert "Arturo" in response

def test_agent_is_working_with_memory_and_history():
    string_to_remember = "Brian's cat is named Arturo"
    memory = LlamaMemory()
    memory.remember_string(string_to_remember)
    agent = Agent(GENERAL,memory)
    prompt = """Please remember that Brian has a green car."""
    agent.make_request(prompt)
    prompt2 = """Please tell me the name of Brian's cats from context and the color of his car from the history"""
    response = agent.make_request(prompt2)
    print(f"Response: {response}")
    assert "Arturo" in response
    assert "green" in response
