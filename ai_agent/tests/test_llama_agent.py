from langchain.prompts import PromptTemplate
from ai_agent import LlamaAgent

def test_initialize_ok_with_mocked_dependencies():
    model = 'test_model'
    agent = LlamaAgent(model, TESTPROMPT)
    assert isinstance(agent,LlamaAgent)

TESTPROMPT = PromptTemplate(
        input_variables=["topic"],
        template ="You are happy chatbot : {topic} ")
