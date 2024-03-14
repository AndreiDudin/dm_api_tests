import pytest

@pytest.fixture
def chrome():
    return 1

@pytest.fixture
def aluminium():
    return 1

@pytest.fixture
def brom():
    return 1


# def test_mix_elements():
#     result = chrome() + aluminium() + brom()
#     assert result == 3

def test_mix_elements_fixture(chrome, aluminium, brom):
    result = chrome + aluminium + brom
    assert result == 3