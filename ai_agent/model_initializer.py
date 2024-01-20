from langchain_community.llms import Ollama
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def initialize_ollama(modelname):
    """ initialize ollamam model - make sure ollama is installed and the appropriate model is pulled
        To pull llama2 - run 'ollama pull <modelname>'"""
    llm = Ollama(model=modelname)
    llm = Ollama(
        model=modelname,
        callbacks=[StreamingStdOutCallbackHandler()]
    )

    return llm
