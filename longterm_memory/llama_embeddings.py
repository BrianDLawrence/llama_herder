""" This is needed because chromadb changed it's interface
    https://docs.trychroma.com/migration#migration-to-0416---november-7-2023
"""
# pylint: disable=redefined-builtin
from langchain_community import embeddings

class LLamaEmbeddings(embeddings.ollama.OllamaEmbeddings):
    def __init__(self, model, *args, **kwargs):
        super().__init__(model=model, *args, **kwargs)

    def _embed_documents(self, texts):
        return super().embed_documents(texts)

    def __call__(self, input):
        return self._embed_documents(input)
