import pytest

def test_addition():
    a = 1
    b = 2
    assert a + b == 3

@pytest.mark.smoke
def test_user_login(sample_data):
    assert sample_data["username"] == "test_user"
