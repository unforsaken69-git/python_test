import pytest

@pytest.fixture
def sample_data():
    print("\n[Setup] 建立資料")
    yield {"username": "test_user", "password": "1234"}
    print("\n[Teardown] 清除資料")
