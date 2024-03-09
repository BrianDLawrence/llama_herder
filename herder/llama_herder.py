"""
This is the program that takes the Goal, the Context,
and creates the required amount of ai agents to do the job. 
"""
from ai_agent import Agent
from config import MAXCONVOS
# pylint: disable=too-few-public-methods

class LlamaHerder:
    """ The class that can herd our llama ai agents """

    __SAFEWORD = "I CAN'T HELP"
    __GOALWORD = "THE GOAL IS COMPLETE!"

    __USERPROMPT = """
        You are the user, you will be given a goal and must ask the right questions 
        to determine if you goal has been achieved.
        If your goal has been achieved, please make sure to say the following
        in all caps: 
        """+__GOALWORD+" Your Chat History is: {history} The request is: {request}"

    __HELPERPROMPT = """
        You are an all purpose helper. You will answer questions to the best of your ability
        with the goal of helping the user. If you can't help anymore, please say the following
        in all caps: 
        """+__SAFEWORD+" Your Chat History is: {history} The request is: {request}"

    def __init__(self, user,helper):
        self.user = Agent(user)
        self.helper = Agent(helper)

    def herd(self, goal, context):
        """ the main herding function """
        userdialog = self.user.make_request_with_template(" The goal is: "+goal+" CONTEXT: "+context,self.__USERPROMPT)
        print(f"Initial User Agent Response: {userdialog}")

        for i in range(MAXCONVOS):
            print(f"Loop: {i+1}")
            helperdialog = self.helper.make_request_with_template(userdialog,self.__HELPERPROMPT)
            print(f"Helper Response: {helperdialog}")
            if LlamaHerder.__GOALWORD in userdialog:
                break
            userdialog = self.user.make_request_with_template(helperdialog, self.__USERPROMPT)
            print(f"User Response: {userdialog}")
            if LlamaHerder.__SAFEWORD in helperdialog:
                break

        return userdialog
