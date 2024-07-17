import re
import requests

class Handler:
    def __init__(self, rag_service_url:str,timeout:int):
        self.rag_service_url = rag_service_url
        self.timeout = timeout

    def process_urls(self, urls):
        response = requests.post(f"{self.rag_service_url}/process-urls", json=urls,timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def parse_urls(self,text:str):
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = url_pattern.findall(text)
        return urls
