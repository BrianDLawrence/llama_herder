from config import GENERAL
from herder import LlamaHerder
from .test_data import MOCKCALENDARDATA1,MOCKTODOLIST1,MOCKGOAL1

def test_herder_initialization():
    """test that the herder initializes OK"""
    herder = LlamaHerder(GENERAL,GENERAL)
    assert isinstance(herder,LlamaHerder)

def test_herder_scenerio_one():
    herder = LlamaHerder(GENERAL,GENERAL)
    response = herder.herd(MOCKGOAL1,f"CALENDAR:{MOCKCALENDARDATA1} TODO:{MOCKTODOLIST1} ")
    print(response)
