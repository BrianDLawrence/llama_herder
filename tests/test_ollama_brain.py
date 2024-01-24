""" Testing ollama brain """
from ai_agent import LlamaBrain

def test_llama_thalamus_prompts():
    """ Testing initialization of the brain """
    brain = LlamaBrain()

    thalamus_prompt = "You are part of a python program. Your only job is to review the following context and help the program redirect to the appropriate LLM. If the context contains a task that would require math or science, respond with the single word of 'LEFT', otherwise respond with a single word 'RIGHT' - ONLY RESPOND with one of those words, nothing else. Here is the context: "
    context = "Here is a daily todo list: Apply to 5 jobs, respond to emails, call the kids, code in python, play guitar "
    brain.think(thalamus_prompt + context)
