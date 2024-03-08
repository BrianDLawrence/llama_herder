from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from longterm_memory import LlamaMemory
from .utils.llm_constants import DEFAULT_TEMPLATE,DEFAULT_TEMPLATE_MEMORY
# pylint: disable=too-few-public-methods

class Agent:

    __default_template = DEFAULT_TEMPLATE
    __default_template_memory = DEFAULT_TEMPLATE_MEMORY

    def __init__(self,model,memory=None):
        self.llm = ChatOllama(model=model)
        self.history = []
        if memory is not None and not isinstance(memory,LlamaMemory):
            raise TypeError("memory must be of type LlamaMemory")
        self.memory = memory

    def make_request(self, request):
        if self.memory is None:
            return self.make_request_with_template(request,self.__default_template)
        return self.make_request_with_template(request,self.__default_template_memory)

    def make_request_with_template(self,request,template):
        chain = self.__create_chain_from_template(template)
        response = chain.invoke(self.__create_request_with_history(request))
        self.__add_response_to_history(response)
        return response

    def __create_chain_from_template(self,template):
        prompt = ChatPromptTemplate.from_template(template)
        if self.memory is None:
            chain = prompt | self.llm | StrOutputParser()
        else:
            chain = ({"context":self.memory.get_memory_as_vectorstore().as_retriever(),
                      "request":RunnablePassthrough(),
                      "history":RunnablePassthrough()}
            | prompt | self.llm | StrOutputParser())
        return chain

    def __create_request_with_history(self,request):
        return {"request":request, "history":self.get_history_as_string()}

    def get_history_as_string(self):
        return " ".join(self.history)

    def __add_response_to_history(self, response):
        self.history.append(response)
