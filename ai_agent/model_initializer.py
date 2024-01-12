from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def initialize_llama2():
    """ initialize ollamam llama2 model - make sure ollama is installed and llama2 is pulled
        To pull llama2 - run 'ollama pull llama2'"""
    llm = Ollama(model="llama2")
    llm = Ollama(
        model="llama2",
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )

    return llm

def initialize_mathwiz():
    """ initialize ollamam wizard-math model - make sure ollama is installed and wizard-math is pulled
    To pull llama2 - run 'ollama pull wizard-math"""
    llm = Ollama(model="wizard-math")
    llm = Ollama(
        model="wizard-math",
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )

    return llm
