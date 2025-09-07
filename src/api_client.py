import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_health(self):
        return requests.get(f"{self.base_url}/get")  # 使用 httpbin 測試
