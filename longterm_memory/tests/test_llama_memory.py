from unittest.mock import patch
from longterm_memory import LlamaMemory

def test_initialize_the_memory():
    memory = LlamaMemory()
    assert isinstance(memory,LlamaMemory)

@patch('longterm_memory.llama_memory.Chroma.from_texts')
@patch('longterm_memory.llama_memory.embeddings.ollama.OllamaEmbeddings')
def test_save_to_memory(mock_ollamaembeddings,mock_from_texts):
    mock_from_texts.return_value = "hello"

    string_to_remember = "THIS IS A string to remember forever"
    memory = LlamaMemory()
    memory.remember_string(string_to_remember)
    assert memory.get_memory_as_vectorstore() == "hello"
    mock_ollamaembeddings.assert_called_once()
    mock_from_texts.assert_called_once()
