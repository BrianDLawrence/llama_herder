from longterm_memory import LlamaMemory

def test_save_to_memory():
    string_to_remember = "THIS IS A string to remember forever"
    memory = LlamaMemory()
    memory.remember_string(string_to_remember)
    vectorstore = memory.get_memory_as_vectorstore()
    assert string_to_remember in str(vectorstore.similarity_search("string"))