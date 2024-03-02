import pytest
from src.auth_jwt import AuthJWT

@pytest.fixture(scope="module")
def Authorize():
    return AuthJWT()
