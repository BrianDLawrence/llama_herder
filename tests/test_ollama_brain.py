""" Testing ollama brain """
from .test_data import MOCKCALENDARDATA1, MOCKTODOLIST1
from ai_agent import LlamaBrain

def test_llama_thalamus_prompts():
    """ Trying to figure out thalamus stuff """
    brain = LlamaBrain()

    thalamus_prompt = "You are part of a python program. Your only job is to review the following context and help the program redirect to the appropriate LLM. If the context contains a task that would require math or science, respond with the single word of 'LEFT', otherwise respond with a single word 'RIGHT' - ONLY RESPOND with one of those words, nothing else. Here is the context: "
    context = "Here is a daily todo list: Apply to 5 jobs, respond to emails, call the kids, code in python, play guitar "
    brain.think(thalamus_prompt + context)

def test_llama_schedule1():
    """ see how the scheduler works """
    brain = LlamaBrain()

    prompt = """ You are an expert scheduler. 
    Your job is to review the calendar data and TODOs and figure out the optimal place for 
    me to complete the TODOs. Please pay attention to the TODOs Description and infer if they are 
    required for any upcoming meetings and make sure to schedule those before the meetings.  
    Please present the list in chronological order mixing TODOS and MEETINGS as appropriate.
    Make sure that the TODOs do NOT overlap with any meetings. 
    Please suggest a time to complete each TODO.
    The schedule should be in the following format exactly:
    [ITEM1 NAME, DATE, START TIME, END TIME, DESCRIPTION], [ITEM2 NAME...]"""

    brain.compute(prompt+" TODO:"+MOCKTODOLIST1+" CALENDAR:"+MOCKCALENDARDATA1)




