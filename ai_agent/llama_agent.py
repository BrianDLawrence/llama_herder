from langchain.chains import LLMChain
from .model_initializer import initialize_ollama
from .utils.error_handling import error_handler
# pylint: disable=too-few-public-methods

class LlamaAgent:

    def __init__(self, model, prompt):
        self.ollama = initialize_ollama(model)
        self.chain = LLMChain(llm=self.ollama, prompt=prompt, verbose=False)
        self.history = []

    def request(self, user_input):
        return self.__handle_history_and_make_request(user_input)

    def __handle_history_and_make_request(self, user_input):
        model_input = self.__add_input_to_history(user_input)
        with error_handler("invoke ollama model"):
            response = self.chain.invoke(model_input)["text"]
        self._add_response_to_history(response)
        return response

    def __add_input_to_history(self, user_input):
        self.history.append(user_input)
        return " ".join(self.history)

    def _add_response_to_history(self, response):
        self.history.append(response)
