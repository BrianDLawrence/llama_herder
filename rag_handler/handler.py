import requests
# pylint: disable=too-few-public-methods

class Handler:
    def __init__(self, rag_service_url:str,timeout:int):
        self.rag_service_url = rag_service_url
        self.timeout = timeout

    def process_urls(self, urls):
        response = requests.post(f"{self.rag_service_url}/process-urls", json=urls,timeout=self.timeout)
        response.raise_for_status()
        return response.json()
