""" LLAMA AGENT """
from langchain.chains import LLMChain
from .model_initializer import initialize_ollama
from .utils.error_handling import error_handler


class LlamaAgent:
    """ Basic agent that remembers """

    def __init__(self, model, prompt):
        self.ollama = initialize_ollama(model)
        self.chain = LLMChain(llm=self.ollama, prompt=prompt, verbose=False)
        self.history = []

    def request(self, user_input):
        """ Invoke the right more creative, intuitive brain  """
        return self.__invoke(user_input, self.chain)

    def __invoke(self, user_input, model):
        """ Invoke the model, make it think """
        # Append the user input to history
        self.history.append(user_input)

        # Create input for the model by concatenating the history
        model_input = " ".join(self.history)

        # compute uses the left brain
        with error_handler("invoke ollama model"):
            response = model.invoke(model_input)["text"]

        # Append the response to history
        self.history.append(response)

        return response
