""" LLAMA BRAIN """
from config import LEFTBRAIN,RIGHTBRAIN,THALAMUS
from .model_initializer import initialize_ollama

class LlamaBrain:
    """ Basically a smarter chatbot that consists of three LLMS """
    def __init__(self):
        self.left = initialize_ollama(LEFTBRAIN)
        self.right = initialize_ollama(RIGHTBRAIN)
        self.thalamus = initialize_ollama(THALAMUS)
        self.history = []

    def think(self, user_input):
        """ Invoke the brain, make it think """
        # Append the user input to history
        self.history.append(user_input)

        # Create input for the model by concatenating the history
        model_input = " ".join(self.history)

        # Generate the response -- currently right brain thinking only, just wait.. work in progress
        response = self.right.invoke(model_input)

        # Append the response to history
        self.history.append(response)

        return response
