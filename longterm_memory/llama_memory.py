from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
import chromadb
from .llama_embeddings import LLamaEmbeddings
# pylint: disable=no-member
# pylint: disable=not-callable

CHUNK_SIZE = 7500
CHUNK_OVERLAP = 100
COLLECTION_NAME = 'mem-chroma'
EMBEDDINGS_MODEL = 'nomic-embed-text'

class LlamaMemory:

    def __init__(self, persistent_location=None):
        self.string_to_remember = None
        self.persistent_location = persistent_location
        if persistent_location:
            self.client = chromadb.PersistentClient(path=persistent_location)
        else:
            self.client = chromadb.PersistentClient()

    def remember_string(self, string_to_remember):
        self.string_to_remember = string_to_remember
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)
        text_splits = text_splitter.split_text(string_to_remember)

        collection = self.client.get_or_create_collection(name=COLLECTION_NAME,
                      embedding_function = LLamaEmbeddings(model=EMBEDDINGS_MODEL))

        collection.upsert(ids=["id1"],documents=text_splits)

    def get_memory_as_vectorstore(self):
        return Chroma(
            client=self.client,
            collection_name=COLLECTION_NAME,
            embedding_function=LLamaEmbeddings(model=EMBEDDINGS_MODEL),
        )
