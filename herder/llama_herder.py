"""
This is the program that takes the Goal, the Context,
and creates the required amount of ai agents to do the job. 
"""
from langchain.prompts import PromptTemplate
from ai_agent import LlamaAgent
from config import MAXCONVOS
# pylint: disable=too-few-public-methods

class LlamaHerder:
    """ The class that can herd our llama ai agents """

    __SAFEWORD = "I CAN'T HELP"
    __GOALWORD = "THE GOAL IS COMPLETE!"

    __USERPROMPT = PromptTemplate(
        input_variables=["topic"],
        template ="""
        You are the user, you will be given a goal and must ask the right questions 
        to determine if you goal has been achieved.
        If your goal has been achieved, please make sure to say the following
        in all caps: 
        """+__GOALWORD+" : {topic} ")

    __HELPERPROMPT = PromptTemplate(
        input_variables=["topic"],
        template="""
        You are an all purpose helper. You will answer questions to the best of your ability
        with the goal of helping the user. If you can't help anymore, please say the following
        in all caps: 
        """+__SAFEWORD+" : {topic} ")

    def __init__(self, user,helper):
        self.__user = LlamaAgent(user,LlamaHerder.__USERPROMPT)
        self.__helper = LlamaAgent(helper,LlamaHerder.__HELPERPROMPT)

    def herder(self, goal, context):
        """ the main herding function """
        userdialog = self.__user.request(" GOAL: "+goal+" CONTEXT: "+context)

        for _ in range(MAXCONVOS):
            helperdialog = self.__helper.request(userdialog)
            userdialog = self.__user.request(helperdialog)
            if LlamaHerder.__GOALWORD in userdialog:
                break
            if LlamaHerder.__SAFEWORD in helperdialog:
                break

        return userdialog
