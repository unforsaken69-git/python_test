import pytest
from src.api_client import APIClient

@pytest.mark.regression
def test_api_health():
    client = APIClient("https://httpbin.org")  # 公開測試API
    response = client.get_health()
    assert response.status_code == 200
