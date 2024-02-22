from config import GENERAL
from herder import LlamaHerder

def test_herder_initialization():
    """test that the herder initializes OK"""
    herder = LlamaHerder(GENERAL,GENERAL)
    assert isinstance(herder,LlamaHerder)
