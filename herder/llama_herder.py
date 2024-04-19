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
        You are the user, you will be given a goal with context.
        The goal and context are: {request} 
        DO NOT try to solve the problem or achieve the goal. 
        Your job is to review the solution provided to you and determine 
        if the goal is achieved. Please respond by saying the following in 
        all caps if the goal has been achieved:
        """+__GOALWORD+ " Your Chat History is: {history} "

    __HELPERPROMPT = """
        You are an all purpose helper. You will try to achieve the goal to the best of your ability.
        If you can't help or achieve this goal, please say the following
        in all caps: 
        """+__SAFEWORD+" Your Chat History is: {history} The request is: {request}"

    def __init__(self, user,helper):
        self.user = Agent(user)
        self.helper = Agent(helper)

    def herd(self, goal, context):
        helperdialog = self.initiate_conversation(goal, context)
        return self.have_conversation_loop(helperdialog)

    def initiate_conversation(self, goal, context):
        userdialog = self.user.make_request_with_template(" The goal is: "+goal+" CONTEXT: "+context,self.__USERPROMPT)
        print(f"Initial User Agent Response: {userdialog}")
        helperdialog = self.helper.make_request_with_template("The goal is: "+goal+" CONTEXT: ",self.__HELPERPROMPT)
        print(f"Initial Helper Agent Response: {helperdialog}")
        return helperdialog


    def have_conversation_loop(self, helperdialog):
        for i in range(MAXCONVOS):
            print(f"Loop: {i+1}")

            userdialog = self.user.make_request_with_template(helperdialog, self.__USERPROMPT)
            print(f"User Response: {userdialog}")
            if LlamaHerder.__GOALWORD in userdialog:
                break

            helperdialog = self.helper.make_request_with_template(userdialog,self.__HELPERPROMPT)
            print(f"Helper Response: {helperdialog}")
            if LlamaHerder.__SAFEWORD in helperdialog:
                userdialog = f"GOAL NOT ACHIEVED: userdialog={userdialog} helperdialog={helperdialog}"
                break

            if i == MAXCONVOS-1:
                userdialog = f"GOAL NOT ACHIEVED MAXATTEMPS: userdialog={userdialog} helperdialog={helperdialog}"
        return userdialog
