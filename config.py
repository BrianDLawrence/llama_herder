""" 
Common Configuration needed for our project
"""
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
load_dotenv()

#Ollama Model for our Llama Agents
MATH = "wizard-math"
GENERAL = "llama2"
GEMMA = "gemma:2b"
TINY = "tinyllama"
MISTRAL = "mistral:instruct"

#max number of conversations allowed
MAXCONVOS = 2

#General Prompt
GENERALPROMPT = PromptTemplate(
        input_variables=["topic"],
        template ="You are happy chatbot : {topic} ")

#CLOUD URL
CLOUDAMQP_URL = os.getenv('CLOUDAMQP_URL','no_CLOUDAMQP_Variable')

#API TIMEOUT
API_CALL_TIMEOUT = 30
