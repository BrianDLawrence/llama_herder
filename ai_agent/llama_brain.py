from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from .model_initializer import initialize_llama2, initialize_mathwiz

class LlamaBrain:
    """ Basically a smarter chatbot that consists of three LLMS """
    def __init__(self):
        self.left = initialize_llama2()
        self.right = initialize_mathwiz()
        self.history = []

    def think(self, user_input):
        """ Invoke the brain, make it think """
        # Append the user input to history
        self.history.append(user_input)

        # Create input for the model by concatenating the history
        model_input = " ".join(self.history)

        # Generate the response -- currently LEFT brain thinking only, just wait.. work in progress
        response = self.left.invoke(model_input)

        # Append the response to history
        self.history.append(response)

        return response

