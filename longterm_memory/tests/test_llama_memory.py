from unittest.mock import patch, MagicMock
from longterm_memory import LlamaMemory

def test_initialize_the_memory():
    memory = LlamaMemory()
    assert isinstance(memory,LlamaMemory)

@patch('longterm_memory.llama_memory.LLamaEmbeddings')
@patch('longterm_memory.llama_memory.chromadb.PersistentClient')
def test_remember_string(mock_persistentclient, mock_ollamaembeddings):
    mock_instance = mock_persistentclient.return_value
    mock_instance.get_or_create_collection = MagicMock()

    string_to_remember = "THIS IS A string to remember forever"
    memory = LlamaMemory()
    memory.remember_string(string_to_remember)

    mock_ollamaembeddings.assert_called_once()
    mock_persistentclient.assert_called_once()
    mock_instance.get_or_create_collection.assert_called_once()

@patch('longterm_memory.llama_memory.chromadb.PersistentClient')
@patch('longterm_memory.llama_memory.Chroma')
@patch('longterm_memory.llama_memory.LLamaEmbeddings')
def test_get_memory_as_vectorstore(mock_ollamaembeddings,mock_chroma,mock_persistentclient):
    mock_vectorstore = mock_chroma.return_value
    memory = LlamaMemory()
    mock_persistentclient.assert_called_once()
    assert memory.get_memory_as_vectorstore() == mock_vectorstore
    mock_chroma.assert_called_once()
    mock_ollamaembeddings.assert_called_once()
