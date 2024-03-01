from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain.text_splitter import CharacterTextSplitter
# pylint: disable=no-member

CHUNK_SIZE = 7500
CHUNK_OVERLAP = 100

class LlamaMemory:

    def __init__(self):
        self.string_to_remember = None
        self.vectorstore = None

    def remember_string(self, string_to_remember):
        self.string_to_remember = string_to_remember
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)
        text_splits = text_splitter.split_text(string_to_remember)
        self.vectorstore = Chroma.from_texts(
            texts = text_splits,
            collection_name = "mem-chroma",
            embedding=embeddings.ollama.OllamaEmbeddings(model='nomic-embed-text')
        )

    def get_memory_as_vectorstore(self):
        return self.vectorstore
