""" test the herder which handles multiple agents
along with goals """
from config import GENERAL
from herder import LlamaHerder
from .test_data import MOCKCALENDARDATA1, MOCKTODOLIST1,MOCKGOAL1

def test_herder_initialization():
    """test that the herder initializes OK"""
    herder = LlamaHerder(GENERAL,GENERAL)
    assert isinstance(herder,LlamaHerder)

#def test_herder_goal1():
    #"""test that the herder initializes OK"""
    #herder = LlamaHerder(GENERAL,GENERAL)
    #herder.herder(MOCKGOAL1,MOCKTODOLIST1+MOCKCALENDARDATA1)
