""" LLAMA BRAIN """
from config import LEFTBRAIN,RIGHTBRAIN,THALAMUS
from .model_initializer import initialize_ollama
from .utils.error_handling import error_handler

class LlamaBrain:
    """ Basically a smarter chatbot that consists of three LLMS """
    def __init__(self):
        self.left = initialize_ollama(LEFTBRAIN)
        self.right = initialize_ollama(RIGHTBRAIN)
        self.thalamus = initialize_ollama(THALAMUS)
        self.history = []

    def think(self, user_input):
        """ Invoke the right more creative, intuitive brain  """
        return self.invoke(user_input, self.right)
    
    def compute(self, user_input):
        """ Invoke the left more logicical analytic brain """
        return self.invoke(user_input, self.left)

    def invoke(self, user_input, brain):
        """ Invoke the brain, make it think """
        # Append the user input to history
        self.history.append(user_input)

        # Create input for the model by concatenating the history
        model_input = " ".join(self.history)
        
        # compute uses the left brain
        with error_handler("invoke ollama model"):
            response = brain.invoke(model_input)

        # Append the response to history
        self.history.append(response)

        return response