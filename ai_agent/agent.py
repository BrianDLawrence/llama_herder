from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from .utils.llm_constants import DEFAULT_TEMPLATE
# pylint: disable=too-few-public-methods

class Agent:

    __default_template = DEFAULT_TEMPLATE

    def __init__(self,model):
        self.llm = ChatOllama(model=model)
        self.history = []

    def make_request(self, request):
        return self.make_request_with_template(request,self.__default_template)

    def make_request_with_template(self,request,template):
        chain = self.__create_chain_from_template(template)
        response = chain.invoke(self.__create_request_with_history(request))
        self.__add_response_to_history(response)
        return response

    def __create_chain_from_template(self,template):
        prompt = ChatPromptTemplate.from_template(template)
        return prompt | self.llm | StrOutputParser()

    def __create_request_with_history(self,request):
        return {"request":request, "history":self.get_history_as_string()}

    def get_history_as_string(self):
        return " ".join(self.history)

    def __add_response_to_history(self, response):
        self.history.append(response)
