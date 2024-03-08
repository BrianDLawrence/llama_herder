import tempfile
from longterm_memory import LlamaMemory

def test_save_to_memory():
    string_to_remember = "THIS IS A string to remember forever"
    memory = LlamaMemory()
    memory.remember_string(string_to_remember)
    vectorstore = memory.get_memory_as_vectorstore()
    assert string_to_remember in str(vectorstore.similarity_search("string"))

def test_save_to_memory_persistent():
    temppath = "/tests/longtermintegrationtest"
    string_to_remember = "THIS IS A string to remember forever"

    with tempfile.TemporaryDirectory() as temppath:
        memory = LlamaMemory(temppath)
        memory.remember_string(string_to_remember)

        memory2 = LlamaMemory(temppath)
        vectorstore = memory2.get_memory_as_vectorstore()
        assert string_to_remember in str(vectorstore.similarity_search("string"))
